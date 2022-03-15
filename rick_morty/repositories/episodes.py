import datetime
from typing import List

from rick_morty.database.models import Episode
from .base import BaseRepository

class EpisodeRepository(BaseRepository):

    def create_episode(self, data: dict) -> dict:
        characters = data.pop("characters")
        episode = Episode(**data)

        for character in  characters:
            episode.characters.append(character)

        with self._session_factory() as session:
            session.add(episode)
            session.commit()
            session.refresh(episode)
            return episode.as_dict()
    
    def get_episodes(self) -> List[dict]:
        with self._session_factory() as session:
            episodes = session.query(Episode).all()
            return [e.as_dict() for e in episodes]

    def get_episode(self, episode_id: int) -> dict:
        with self._session_factory() as session:
            episode = session.query(Episode).filter(Episode.id == episode_id).first()
            if episode is None:
                return {}
            return episode.as_dict()