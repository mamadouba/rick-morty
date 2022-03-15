from typing import List
from rick_morty.database.models import Episode, Character
from .base import BaseRepository

class EpisodeRepository(BaseRepository):

    def create_episode(self, data: dict) -> dict:
        character_ids = data.pop("characters")
        episode = Episode(**data)

        with self._session_factory() as session:
            for _id in character_ids:
                query = session.query(Character)
                character = query.filter(Character.id == _id).first()
                if not character:
                    episode.characters.append(character)
            session.add(episode)
            session.commit()
            session.refresh(episode)
            return episode.as_dict()
    
    def get_episodes(self) -> List[dict]:
        with self._session_factory() as session:
            episodes = session.query(Episode).all()
            return [episode.as_dict() for episode in episodes]

    def get_episode(self, episode_id: int) -> dict:
        with self._session_factory() as session:
            episode = session.query(Episode).filter(Episode.id == episode_id).first()
            if episode is None:
                return {}
            return episode.as_dict()