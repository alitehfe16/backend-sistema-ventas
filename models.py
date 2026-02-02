from sqlalchemy import Column, Integer, String, Numeric, DateTime
from database import Base

class Producto(Base):
    __tablename__ = "productos"  # usa el nombre REAL de tu tabla

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Numeric, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime)
