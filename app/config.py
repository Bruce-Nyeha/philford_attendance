from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / "migrations" / ".env" 
load_dotenv(dotenv_path=env_path)
class Settings(BaseSettings):
    DATABASE_URL : str = os.getenv("DATABASE_URL")
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: str = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
class Config:
    env_file = ".env"

settings = Settings()
