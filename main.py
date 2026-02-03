from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from database import Base, engine, get_db
from models import Producto

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoOut(ProductoCreate):
    id: int

    class Config:
        orm_mode = True

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/productos", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo = Producto(**producto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/productos", response_model=List[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

