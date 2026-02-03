from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/productos")
def crear_producto(producto: Producto):
    with engine.begin() as conn:
        conn.execute(
            text(
                "INSERT INTO productos (nombre, precio, stock) VALUES (:nombre, :precio, :stock)"
            ),
            {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock,
            },
        )
    return {"mensaje": "Producto guardado en Supabase"}

@app.get("/productos", response_model=List[Producto])
def listar_productos():
    with engine.begin() as conn:
        result = conn.execute(
            text("SELECT nombre, precio, stock FROM productos")
        ).mappings().all()
    return result
