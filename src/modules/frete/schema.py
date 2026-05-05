from pydantic import BaseModel, Field

class FreteBase(BaseModel):
    destino: str = Field(..., min_length=1)
    peso: float = Field(..., gt=0)
    transportadora: str = Field(..., min_length=1)

class FreteCreate(FreteBase):
    pass

class FreteUpdate(BaseModel):
    destino: str | None = Field(None, min_length=1)
    peso: float | None = Field(None, gt=0)
    transportadora: str | None = Field(None, min_length=1)

class FreteResponse(FreteBase):
    id: int

    class Config:
        from_attributes = True
