from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os

# =====================
# CONFIGURACIÓN DB
# =====================
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# =====================
# MODELO DB
# =====================
class ProductoDB(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

# =====================
# FASTAPI
# =====================
app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

# =====================
# DEPENDENCIA DB
# =====================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =====================
# ENDPOINTS
# =====================
@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/productos")
def crear_producto(producto: Producto, db: Session = Depends(get_db)):
    nuevo = ProductoDB(
        nombre=producto.nombre,
        precio=producto.precio,
        stock=producto.stock
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Producto guardado en Supabase", "id": nuevo.id}

@app.get("/productos", response_model=List[Producto])
def listar_productos(db: Session = Depends(get_db)):
    productos = db.query(ProductoDB).all()
    return productos
