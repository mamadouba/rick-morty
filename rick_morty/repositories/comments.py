from typing import List
from rick_morty.database.models import Comment
from rick_morty.utils import apply_filter 
from .base import BaseRepository

class CommentRepository(BaseRepository):

    def create_comment(self, **data: dict) -> dict:
        comment = Comment(**data)
            
        with self._session_factory() as session:
            session.add(comment)
            session.commit()
            session.refresh(comment)
            return comment.as_dict()
    
    def get_comments(self, page: int, per_page: int, filters: str) -> dict:
        with self._session_factory() as session:
            query = session.query(Comment)
            total = query.count()
            query = query.limit(per_page).offset((page - 1) * per_page)
            items =  [item.as_dict() for item in query.all()]

            if filters:
                items = [apply_filter(item, filters) for item in items]
            
            return {
                "data": items,
                "total": total,
                "current_page": page,
                "per_page": per_page
            }

    def get_comment(self, comment_id: int) -> dict:
        with self._session_factory() as session:
            comment = session.query(Comment).filter(Comment.id == comment_id).first()
            if comment is None:
                return {}
            return comment.as_dict()

    def delete_comment(self, comment_id: int) -> dict:
        with self._session_factory() as session:
            comment = session.query(Comment).filter(Comment.id == comment_id).first()
            if comment is None:
                return {}
            session.delete(comment)
            session.commit()
            return comment.as_dict()

    def export_comments(self) -> dict:
        with self._session_factory() as session:
            comments = session.query(Comment).all()
            if comments is None:
                return {}
            return [comment.as_dict() for comment in comments]

    
