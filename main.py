from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ===== MODELO =====
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

# ===== ENDPOINT BASE =====
@app.get("/")
def root():
    return {"status": "ok"}

# ===== CREAR PRODUCTO (AÚN NO GUARDA EN SUPABASE) =====
@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "mensaje": "Producto recibido correctamente",
        "producto": producto
    }

# ===== LISTAR PRODUCTOS (MOCK) =====
@app.get("/productos", response_model=List[Producto])
def listar_productos():
    return [
        {"nombre": "Taladro", "precio": 500, "stock": 10},
        {"nombre": "Amoladora", "precio": 350, "stock": 5}
    ]
