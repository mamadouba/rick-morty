from typing import Optional
from pydantic import BaseSettings 

class Settings(BaseSettings):
    env: Optional[str] = "dev"
    
    db_host: str 
    db_port: str 
    db_name: str
    db_user: str 
    db_password: str

    jwt_secret: str 
    jwt_duration: Optional[int] = 3600  
    jwt_algorithm: Optional[str] = "HS256"

    @property
    def db_uri(cls):
        if cls.env == "dev":
            return "sqlite:////tmp/app.db" 
        return f"postgresql://{cls.db_user}:{cls.db_password}@{cls.db_host}:{cls.db_port}/{cls.db_name}"
    
settings = Settings()

