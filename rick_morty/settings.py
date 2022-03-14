from pydantic import BaseSettings 

class Settings(BaseSettings):
    db_host: str 
    db_port: str 
    db_name: str
    db_user: str 
    db_password: str

    @property
    def psql_conn_str(cls):
        return f"postgresql://{cls.db_user}:{cls.db_password}@{cls.db_host}:{cls.db_port}/{cls.db_name}" 
    
    @property
    def sqlite_conn_str(cls):
        return "sqlite:///app.db" 
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
