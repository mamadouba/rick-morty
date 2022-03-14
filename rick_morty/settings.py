from pydantic import BaseSettings 

class Settings(BaseSettings):
    db_host: str 
    db_port: str 
    db_name: str
    db_login: str 
    db_password: str

    @property
    def psql_conn_str(cls):
        return f"postgresql://{cls.login}:{cls.db_password}@{cls.host}:{cls.port}/{cls.db_name}" 
    
    @property
    def sqlite_conn_str(cls):
        return "sqlite:///app.db" 
    
    class Config:
        env_file: "app.env"

settings = Settings()
