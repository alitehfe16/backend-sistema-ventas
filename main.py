from fastapi import FastAPI
from pydantic import BaseModel
import os
from sqlalchemy import create_engine, text

app = FastAPI()

# conexión a Supabase (Railway ya tiene esta variable)
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/productos")
def crear_producto(producto: Producto):
    with engine.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO productos (nombre, precio, stock) "
                "VALUES (:nombre, :precio, :stock)"
            ),
            {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            }
        )
        conn.commit()

    return {"mensaje": "Producto guardado"}
