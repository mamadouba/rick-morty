from typing import List
from rick_morty.database.models import User
from .base import BaseRepository


class UserRepository(BaseRepository):
    def create_user(self, **data: dict) -> dict:
        user = User(**data)
        with self._session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user.as_dict()

    def get_users(self) -> List[dict]:
        with self._session_factory() as session:
            users = session.query(User).all()
            return [user.as_dict() for user in users]

    def get_user(self, user_id: int) -> dict:
        with self._session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user is None:
                return None
            return user.as_dict()

    def find_user(self, email: str) -> dict:
        with self._session_factory() as session:
            user = session.query(User).filter(User.email == email).first()
            if user:
                data = user.as_dict()
                data["password_hash"] = user.password_hash
                return data
            return {}

    def delete_user(self, user_id: int) -> dict:
        with self._session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user is None:
                return None
            user.delete(user)
            session.commit()
            return user.as_dict()
