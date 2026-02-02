from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"ok": True}

@app.post("/productos")
def crear_producto(nombre: str, precio: float, stock: int, db: Session = Depends(get_db)):
    producto = models.Producto(
        nombre=nombre,
        precio=precio,
        stock=stock
    )
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

