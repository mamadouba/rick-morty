from typing import List, Optional
from pydantic import BaseModel

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

class EpisodeList(BaseModel):
    data: List[EpisodeOut]
    total: int 
    page: int 
    per_page: int 