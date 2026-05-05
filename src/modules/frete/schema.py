from pydantic import BaseModel, Field

class FreteBase(BaseModel):
    destino: str = Field(..., min_length=1)
    peso: float = Field(..., gt=0)
    transportadora: str = Field(..., min_length=1)

class FreteCreate(FreteBase):
    pass

class FreteResponse(FreteBase):
    id: int

    class Config:
        from_attributes = True
