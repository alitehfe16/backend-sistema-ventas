import os
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"  # ASEGÚRATE que este nombre es el real en Supabase

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Numeric, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}

@app.post("/productos")
def crear_producto(nombre: str, precio: float, stock: int):
    db = SessionLocal()
    try:
        producto = Producto(
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
