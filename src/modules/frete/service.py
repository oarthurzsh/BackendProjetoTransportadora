from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .repository import FreteRepository
from .schema import FreteCreate, FreteUpdate

class FreteService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = FreteRepository()

    def create_frete(self, frete_data: FreteCreate):
        return self.repository.create(self.db, frete_data)

    def list_fretes(self):
        return self.repository.get_all(self.db)

    def update_frete(self, frete_id: int, frete_data: FreteUpdate):
        db_frete = self.repository.get_by_id(self.db, frete_id)
        if not db_frete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frete não encontrado")
        
        return self.repository.update(self.db, db_frete, frete_data.model_dump(exclude_unset=True))

    def delete_frete(self, frete_id: int):
        db_frete = self.repository.get_by_id(self.db, frete_id)
        if not db_frete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Frete não encontrado")
        
        self.repository.delete(self.db, db_frete)
        return {"message": "Frete deletado com sucesso"}
