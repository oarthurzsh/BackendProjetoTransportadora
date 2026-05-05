from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from .service import FreteService
from .schema import FreteCreate, FreteResponse, FreteUpdate
from typing import List

router = APIRouter(prefix="/fretes", tags=["fretes"])

@router.post("/", response_model=FreteResponse, status_code=status.HTTP_201_CREATED)
def create_frete(
    frete_data: FreteCreate,
    db: Session = Depends(get_db)
):
    service = FreteService(db)
    return service.create_frete(frete_data)

@router.get("/", response_model=List[FreteResponse])
def list_all(db: Session = Depends(get_db)):
    service = FreteService(db)
    return service.list_fretes()

@router.put("/{frete_id}", response_model=FreteResponse)
def update_frete(
    frete_id: int,
    frete_data: FreteUpdate,
    db: Session = Depends(get_db)
):
    service = FreteService(db)
    return service.update_frete(frete_id, frete_data)

@router.delete("/{frete_id}")
def delete_frete(frete_id: int, db: Session = Depends(get_db)):
    service = FreteService(db)
    return service.delete_frete(frete_id)

