from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Producto

app = FastAPI()

# Crear tablas en Supabase (si no existen)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/productos")
def crear_producto(
    nombre: str,
    precio: float,
    stock: int,
    db: Session = Depends(get_db)
):
    producto = Producto(
        nombre=nombre,
        precio=precio,
        stock=stock
    )
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

@app.get("/productos")
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

