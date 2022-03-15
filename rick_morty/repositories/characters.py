from typing import List
from rick_morty.database.models import Character
from .base import BaseRepository

class CharacterRepository(BaseRepository):

    def create_character(self, data: dict) -> dict:
        character = Character(**data)
        with self._session_factory() as session:
            session.add(character)
            session.commit()
            session.refresh(character)
            return character.as_dict()
    
    def get_characters(self) -> List[dict]:
        with self._session_factory() as session:
            result = session.query(Character).all()
            return [r.as_dict() for r in result]

    def get_character(self, character_id: int) -> dict:
        with self._session_factory() as session:
            character = session.query(Character).filter(Character.id == character_id).first()
            if character is None:
                return {}
            return character.as_dict()

    
