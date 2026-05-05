from pydantic import BaseModel, Field
from datetime import datetime

class FreteBase(BaseModel):
    destino: str | None = Field(None)
    cep: str | None = Field(None, min_length=8, max_length=10)
    estado: str | None = Field(None, min_length=2, max_length=2)
    cidade: str | None = Field(None)
    bairro: str | None = Field(None)
    logradouro: str | None = Field(None)
    numero: str | None = Field(None)
    peso: float = Field(..., gt=0)
    transportadora: str = Field(..., min_length=1)
    descricao: str | None = Field(None)

class FreteCreate(FreteBase):
    pass

class FreteUpdate(BaseModel):
    destino: str | None = Field(None)
    cep: str | None = Field(None)
    estado: str | None = Field(None)
    cidade: str | None = Field(None)
    bairro: str | None = Field(None)
    logradouro: str | None = Field(None)
    numero: str | None = Field(None)
    peso: float | None = Field(None, gt=0)
    transportadora: str | None = Field(None, min_length=1)
    descricao: str | None = Field(None)

class FreteResponse(FreteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
