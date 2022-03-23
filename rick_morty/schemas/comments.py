from typing import List, Optional
from pydantic import BaseModel


class Comment(BaseModel):
    episode_id: Optional[int]
    character_id: Optional[int]
    comment: str

    class Config:
        orm_mode: True


class CommentIn(Comment):
    pass


class CommentOut(Comment):
    id: int


class CommentList(BaseModel):
    data: List[CommentOut]
    total: int
    page: int
    per_page: int
