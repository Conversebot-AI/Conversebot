import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    
    SECRET_KEY:str = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI:str = os.environ.get("SQLALCHEMY_DATABASE_URI")
    DATABASE_NAME:str = os.environ.get('DATABASE_NAME')
    DATABASE_USER:str = os.environ.get('DATABASE_USER')
    DATABASE_PASS:str = os.environ.get('DATABASE_PASS')
    DATABASE_HOST:str = os.environ.get('DATABASE_HOST')
    DATABASE_PORT:str = os.environ.get('DATABASE_PORT')

settings = Settings()