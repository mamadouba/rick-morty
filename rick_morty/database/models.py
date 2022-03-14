
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(70), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    name = Column(String(30), nullable=False, unique=True)
    episodes = relationship("Episode", secondary='episodecharacters')

class Episode(Base):
    __tablename__ = 'episodes'
    name = Column(String(30), nullable=False, unique=True)
    episode = Column(String(30), nullable=False, unique=True)
    air_date = Column(Date, nullable=False)
    characters = relationship("Character", secondary='episodecharacters')

class EpisodeCharacter(Base):
    __tablename__ = 'episodecharacters'
    episode_id = Column(Integer, ForeignKey("episodes.id"), primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)

class Comment(Base):
    __tablename__ = 'comments'
    episode_id = Column(Integer, ForeignKey("episodes.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))
    comment = Column(String(500), nullable=False)

