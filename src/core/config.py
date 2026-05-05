import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "TransCarga"
    database_url: str = os.getenv("DATABASE_URL", "")
    
    # Support for SUPABASE_URL if DATABASE_URL is empty
    if not database_url:
        database_url = os.getenv("SUPABASE_URL", "")

    # Fix for psycopg2 driver
    if database_url and database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+psycopg2://", 1)

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
