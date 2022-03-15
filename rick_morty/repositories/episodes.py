from typing import List
from rick_morty.database.models import Episode, Character
from rick_morty.utils import apply_filter 
from .base import BaseRepository

class EpisodeRepository(BaseRepository):

    def create_episode(self, data: dict) -> dict:
        character_ids = data.pop("characters")
        episode = Episode(**data)

        with self._session_factory() as session:
            for _id in character_ids:
                query = session.query(Character)
                character = query.filter(Character.id == _id).first()
                if character:
                    episode.characters.append(character)
            session.add(episode)
            session.commit()
            session.refresh(episode)
            return episode.as_dict()
    
    def get_episodes(self, page: int, per_page: int, filters: str) -> dict:
        with self._session_factory() as session:
            query = session.query(Episode)
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
            

    def get_episode(self, episode_id: int) -> dict:
        with self._session_factory() as session:
            episode = session.query(Episode).filter(Episode.id == episode_id).first()
            if episode is None:
                return {}
            return episode.as_dict()