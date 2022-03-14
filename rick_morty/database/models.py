
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'

episode_character = Table(
    'episode_character',
    Base.metadata,
    Column('character_id', ForeignKey('characters.id')),
    Column('episode_id', ForeignKey('episodes.id'))
)

class Character(Base):
    __tablename__ = 'characters'
    name = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    episodes = relationship(
        "Episode",
        secondary=episode_character,
        back_populates='characters')

class Episode(Base):
    __tablename__ = 'episodes'
    name = Column(String(30), nullable=False, unique=True)
    episode = Column(String(30), nullable=False, unique=True)
    air_date = Column(String(30), nullable=False)
    characters = relationship(
        "Character",
        secondary=episode_character,
        back_populates="episodes")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    episode_id = Column(Integer, ForeignKey("episodes.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))
    comment = Column(String(500), nullable=False)

