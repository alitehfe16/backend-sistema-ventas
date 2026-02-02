from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "mensaje": "Producto recibido",
        "producto": producto
    }

