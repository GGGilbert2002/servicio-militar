from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Recluta(Base):
    __tablename__ = "reclutas"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    parroquia = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    apto = Column(Boolean, default=True)
    estatura = Column(Float, nullable=True)
    peso = Column(Float, nullable=True)
    observaciones = Column(String, nullable=True)