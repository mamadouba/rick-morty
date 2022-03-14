from typing import List, Callable
from rick_morty.exceptions import NotFoundError, ConflictError
from rick_morty.database.models import Comment
from .base import BaseRepository

class CommentRepository(BaseRepository):


    def create_comment(self, data: dict) -> Comment:
        comment = Comment(
            id=data.get("id"),
            comment=data.get("comment"),
            character_id=data.get("character_id"),
            episode_id=data.get("episode_id")
        )
        
        with self._session_factory() as session:
            session.add(comment)
            session.commit()
            session.refresh(comment)
            return comment
    
    def get_comments(self) -> List[Comment]:

        with self._session_factory() as session:
            return session.query(Comment).all()

    def get_comment_by_id(self, comment_id: int) -> Comment:
        with self._session_factory() as session:
            comment: Comment = session.query(Comment).filter(Comment.id == comment_id).first()
            if comment is None:
                raise NotFoundError("comment",  "id", comment_id)
            return comment

    def delete_comment(self, comment_id: int) -> None:
        with self._session_factory() as session:
            comment: Comment = session.query(Comment).filter(Comment.id == comment_id).first()
            if comment is None:
                raise NotFoundError("comment",  "id", comment_id)
            comment.delete(comment)
            session.commit()
        

    
