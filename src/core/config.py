import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings(BaseSettings):
    app_name: str = "TransCarga"
    
    database_url_env: str = Field(default="", alias="DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @computed_field
    @property
    def database_url(self) -> str:
        url = os.getenv("DATABASE_URL") or self.database_url_env
        
        if not url:
            return "sqlite:///./transcarga.db"

        if url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
            
        return url

settings = Settings()
