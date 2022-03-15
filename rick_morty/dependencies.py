from functools import lru_cache
from rick_morty.database import Database
from rick_morty.repositories import Repository
from rick_morty.settings import Settings

@lru_cache
def get_settings() -> Settings:
    return Settings()

@lru_cache
def get_db() -> Database:
    settings = get_settings()
    return Database(settings.psql_conn_str)

@lru_cache
def get_repository() -> Repository:
    db = get_db()
    return Repository(session_factory=db.session)
   
