from typing import List, Optional
from pydantic import BaseModel

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
