from typing import List
from rick_morty.exceptions import NotFoundError, ConflictError
from rick_morty.database.models import Character
from .base import BaseRepository

class UserRepository(BaseRepository):

    def character_exists(self, name: str) -> bool:
        with self._session_factory() as session:
            return session.query(Character).filter(Character.name==name).count() > 0

    def create_character(self, name: str) -> Character:
        character = Character(name = name)
        
        with self._session_factory() as session:
            if session.query(Character).filter(Character.name == name).count() > 0:
                raise ConflictError("character", "name", name)
            session.add(character)
            session.commit()
            session.refresh(character)
            return character
    
    def get_characters(self) -> List[Character]:
        with self._session_factory() as session:
            return session.query(Character).all()

    def get_character_by_id(self, character_id: int) -> Character:
        with self._session_factory() as session:
            character: Character = session.query(Character).filter(Character.id == character_id).first()
            if character is None:
                raise NotFoundError("character",  "id", character_id)
            return character

    def delete_character(self, character_id: int) -> None:
        with self._session_factory() as session:
            character: Character = session.query(Character).filter(Character.id == character_id).first()
            if character is None:
                raise NotFoundError("character",  "id", character_id)
            character.delete(character)
            session.commit()
        

    
