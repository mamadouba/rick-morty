from typing import List
from rick_morty.database.models import Character
from rick_morty.utils import apply_filter
from .base import BaseRepository


class CharacterRepository(BaseRepository):
    def create_character(self, data: dict) -> dict:
        character = Character(**data)
        with self._session_factory() as session:
            session.add(character)
            session.commit()
            session.refresh(character)
            return character.as_dict()

    def get_characters(self, page: int, per_page: int, filters: str) -> dict:
        with self._session_factory() as session:
            query = session.query(Character)
            total = query.count()
            query = query.limit(per_page).offset((page - 1) * per_page)
            items = [item.as_dict() for item in query.all()]

            if filters:
                items = [apply_filter(item, filters) for item in items]

            return {
                "data": items,
                "total": total,
                "current_page": page,
                "per_page": per_page,
            }

    def get_character(self, character_id: int) -> dict:
        with self._session_factory() as session:
            character = (
                session.query(Character).filter(Character.id == character_id).first()
            )
            if not character:
                return {}
            return character.as_dict()
