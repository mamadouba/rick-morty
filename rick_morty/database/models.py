
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from . import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

class Character(Base):
    __tablename__ = "characters"
    name = Column(String(30), nullable=False, unique=True)

class Episode(Base):
    __tablename__ = "episodes"

    name = Column(String(30), nullable=False, unique=True)
    episode = Column(String(30), nullable=False, unique=True)
    air_date = Column(Date, nullable=False)

class EpisodeCharacters(Base):
    __tablename__ = "episode_characters"
    episode_id = Column(Integer, nullable=False, unique=True)
    character_id = Column(Integer, nullable=False)

class Comment(Base):
    __tablename__ = "comments"

    actor_id = Column(Integer, nullable=False, ForeignKey=True)
    episode_id = Column(Integer, nullable=False, ForeignKey=True)
    comment = Column(String(200), nullable=False)
