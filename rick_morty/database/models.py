
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
    
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "spicies": self.species,
            "type": self.type,
            "gender": self.gender,
            "episodes": [e.id for e in self.episodes]
        }


class Episode(Base):
    __tablename__ = 'episodes'
    name = Column(String(30), nullable=False, unique=True)
    episode = Column(String(30), nullable=False, unique=True)
    air_date = Column(String(30), nullable=False)
    characters = relationship(
        "Character",
        secondary=episode_character,
        back_populates="episodes")

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "episode": self.episode,
            "air_date": self.air_date,
            "characters": [c.id for c in self.characters]
        }

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    episode_id = Column(Integer, ForeignKey("episodes.id"), nullable=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    comment = Column(String(500), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "episode_id": self.episode_id,
            "character_id": self.character_id,
            "comment": self.comment
        }

