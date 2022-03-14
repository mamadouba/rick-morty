from typing import List
from pydantic import BaseModel

class Message(BaseModel):
    message: str


class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    episode: List[int]

    class Config:
        orm_mode: True

class CharacterIn(Character):
    pass

class CharacterOut(Character):
    pass


class Comment(BaseModel):
    episode_id: int
    character_id: int
    comment: str

    class Config:
        orm_mode: True

class CommentIn(Comment):
    pass

class CommentOut(Comment):
    id: int


class Episode(BaseModel):
    id: int
    name: str 
    episode: str 
    air_date: str
    characters: List[int] 

    class Config:
        orm_mode: True

class EpisodeIn(Episode):
    pass

class EpisodeOut(Episode):
    pass