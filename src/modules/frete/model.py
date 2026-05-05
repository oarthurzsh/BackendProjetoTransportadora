from sqlalchemy import Column, Integer, String, Float
from src.core.database import Base

class Frete(Base):
    __tablename__ = "fretes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    destino = Column(String(255), nullable=False)
    peso = Column(Float, nullable=False)
    transportadora = Column(String(255), nullable=False)
