from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from src.core.database import Base

class Frete(Base):
    __tablename__ = "fretes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    destino = Column(String(255), nullable=True) # Mantido por compatibilidade
    cep = Column(String(10), nullable=True)
    estado = Column(String(2), nullable=True)
    cidade = Column(String(100), nullable=True)
    bairro = Column(String(100), nullable=True)
    logradouro = Column(String(255), nullable=True)
    numero = Column(String(20), nullable=True)
    peso = Column(Float, nullable=False)
    transportadora = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
