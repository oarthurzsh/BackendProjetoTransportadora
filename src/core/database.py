from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.core.config import settings
import logging

# Configuração de log básica
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if not settings.database_url:
    raise ValueError(
        "A URL do banco de dados não foi configurada. "
        "Certifique-se de que DATABASE_URL ou SUPABASE_URL esteja no seu arquivo .env"
    )

logger.info(f"Conectando ao banco de dados: {settings.database_url}")

# Argumentos extras para SQLite
connect_args = {}
if settings.database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.database_url,
    echo=False,  # Reduz ruído de logs do SQLAlchemy
    pool_pre_ping=True,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
