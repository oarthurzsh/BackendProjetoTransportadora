from sqlalchemy.orm import Session
from .repository import FreteRepository
from .schema import FreteCreate

class FreteService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = FreteRepository()

    def create_frete(self, frete_data: FreteCreate):
        return self.repository.create(self.db, frete_data)

    def list_fretes(self):
        return self.repository.get_all(self.db)
