from sqlalchemy.orm import Session
from .model import Frete
from .schema import FreteCreate

class FreteRepository:
    @staticmethod
    def create(db: Session, frete_data: FreteCreate) -> Frete:
        db_frete = Frete(**frete_data.model_dump())
        db.add(db_frete)
        db.commit()
        db.refresh(db_frete)
        return db_frete

    @staticmethod
    def get_all(db: Session) -> list[Frete]:
        return db.query(Frete).all()
