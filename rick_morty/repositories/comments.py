from typing import List, Callable
from rick_morty.database.models import Comment
from .base import BaseRepository

class CommentRepository(BaseRepository):

    def create_comment(self, data: dict) -> Comment:
        comment = Comment(**data)
            
        with self._session_factory() as session:
            session.add(comment)
            session.commit()
            session.refresh(comment)
            return comment
    
    def get_comments(self) -> List[Comment]:
        with self._session_factory() as session:
            return session.query(Comment).all()

    def get_comment(self, comment_id: int) -> Comment:
        with self._session_factory() as session:
            comment = session.query(Comment).filter(Comment.id == comment_id).first()
            return comment

    def delete_comment(self, comment_id: int) -> bool:
        with self._session_factory() as session:
            comment = session.query(Comment).filter(Comment.id == comment_id).first()
            if comment:
                session.delete(comment)
                session.commit()
                return True
            return False 


    
