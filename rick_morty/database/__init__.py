import datetime
import logging
from typing import Callable
from contextlib import contextmanager
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, Session

class Base:

    id = Column(Integer, primary_key=True, autoincrement=True)
   
    def __str__(self):
        return f"{type(self).__name__} id={self.id}"

Base = declarative_base(cls=Base)

logger = logging.getLogger(__name__)

class Database:
    
    def __init__(self, db_url: str):
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = scoped_session(
            sessionmaker(
                bind=self._engine,
                autocommit=False,
                autoflush=False
            )
        )

    def create_database(self) -> None:
        return Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable:
        session: Session = self._session_factory()
        try:
            yield session 
        except Exception:
            logger.exception("rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
