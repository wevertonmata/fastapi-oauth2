from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade'
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = 'sh0ZulJK4UJLq_qYf2Xa1mJ6yRlFIgVCcHozydZImE4'
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
settings = Settings()