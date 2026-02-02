from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

# Endpoint base
@app.get("/")
def root():
    return {"status": "ok"}

# Endpoint de prueba (SIN base de datos)
@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "mensaje": "Producto recibido correctamente",
        "producto": producto
    }

# Endpoint de listado falso (mock)
@app.get("/productos", response_model=List[Producto])
def listar_productos():
    return [
        {"nombre": "Taladro", "precio": 500, "stock": 10},
        {"nombre": "Amoladora", "precio": 350, "stock": 5}
    ]
