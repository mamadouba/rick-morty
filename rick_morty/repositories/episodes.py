import datetime
from typing import List

from rick_morty.database.models import Episode
from .base import BaseRepository

class EpisodeRepository(BaseRepository):

    def create_episode(self, data: dict) -> Episode:
        characters = data.pop("characters")
        episode = Episode(**data)

        for character in  characters:
            episode.characters.append(character)

        with self._session_factory() as session:
            session.add(episode)
            session.commit()
            session.refresh(episode)
            return episode
    
    def get_episodes(self) -> List[Episode]:
        with self._session_factory() as session:
            episodes = session.query(Episode).all()
            return episodes

    def get_episode(self, episode_id: int) -> Episode:
        with self._session_factory() as session:
            episode = session.query(Episode).filter(Episode.id == episode_id).first()
            return episode