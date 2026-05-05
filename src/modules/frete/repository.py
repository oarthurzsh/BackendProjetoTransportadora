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

    @staticmethod
    def get_by_id(db: Session, frete_id: int) -> Frete | None:
        return db.query(Frete).filter(Frete.id == frete_id).first()

    @staticmethod
    def update(db: Session, db_frete: Frete, frete_data: dict) -> Frete:
        for key, value in frete_data.items():
            if value is not None:
                setattr(db_frete, key, value)
        db.commit()
        db.refresh(db_frete)
        return db_frete

    @staticmethod
    def delete(db: Session, db_frete: Frete) -> None:
        db.delete(db_frete)
        db.commit()
