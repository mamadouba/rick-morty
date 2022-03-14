from typing import List, Callable
from rick_morty.exceptions import NotFoundError, ConflictError
from rick_morty.database.models import User
from .base import BaseRepository

class UserRepository(BaseRepository):

    def user_exists(self, username: str) -> bool:
        with self._session_factory() as session:
            return session.query(User).filter(User.username==username).count() > 0

    def create_user(self, username: str, password: str) -> User:
        user = User(
            username = username,
            password = password
        )
        
        with self._session_factory() as session:
            if session.query(User).filter(User.username == username).count() > 0:
                raise ConflictError("user", "username", username)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
    
    def get_users(self) -> List[User]:
        with self._session_factory() as session:
            return session.query(User).all()

    def get_user_by_id(self, user_id: int) -> User:
        with self._session_factory() as session:
            user: User = session.query(User).filter(User.id == user_id).first()
            if user is None:
                raise NotFoundError("user",  "id", user_id)
            return user

    def delete_user(self, user_id: int) -> None:
        with self._session_factory() as session:
            user: User = session.query(User).filter(User.id == user_id).first()
            if user is None:
                raise NotFoundError("user",  "id", user_id)
            user.delete(user)
            session.commit()
        

    
