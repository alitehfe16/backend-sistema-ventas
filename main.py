from fastapi import FastAPI
from database import SessionLocal
import models

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}

@app.post("/productos")
def crear_producto(nombre: str, precio: float, stock: int):
    db = SessionLocal()
    try:
        producto = models.Producto(
            nombre=nombre,
            precio=precio,
            stock=stock
        )
        db.add(producto)
        db.commit()
        db.refresh(producto)
        return {
            "id": producto.id,
            "nombre": producto.nombre,
            "precio": float(producto.precio),
            "stock": producto.stock
        }
    finally:
        db.close()
