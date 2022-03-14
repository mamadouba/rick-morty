from os import stat
from typing import List
from rick_morty.database.models import Character
from .base import BaseRepository

class CharacterRepository(BaseRepository):

    def create_character(self, data: dict) -> Character:
        character = Character(**data)
        with self._session_factory() as session:
            session.add(character)
            session.commit()
            session.refresh(character)
            return character
    
    def get_characters(self) -> List[Character]:
        with self._session_factory() as session:
            result = session.query(Character).all()
            return result

    def get_character(self, character_id: int) -> Character:
        with self._session_factory() as session:
            character = session.query(Character).filter(Character.id == character_id).first()
            return character 

    
