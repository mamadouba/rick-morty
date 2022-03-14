import datetime
from typing import List
from rick_morty.exceptions import NotFoundError, ConflictError
from rick_morty.database.models import Episode
from .base import BaseRepository

class UserRepository(BaseRepository):

    def episode_exists(self, name: str) -> bool:
        with self._session_factory() as session:
            return session.query(Episode).filter(Episode.name==name).count() > 0

    def create_episode(self, name: str, episode: str, air_date: datetime.Date) -> Episode:
        episode = Episode(name=name, episode=episode, air_date=air_date)
        
        with self._session_factory() as session:
            if session.query(Episode).filter(Episode.name == name).count() > 0:
                raise ConflictError("episode", "name", name)
            session.add(episode)
            session.commit()
            session.refresh(episode)
            return episode
    
    def get_episodes(self) -> List[Episode]:
        with self._session_factory() as session:
            return session.query(Episode).all()

    def get_episode_by_id(self, episode_id: int) -> Episode:
        with self._session_factory() as session:
            episode: Episode = session.query(Episode).filter(Episode.id == episode_id).first()
            if episode is None:
                raise NotFoundError("episode",  "id", episode_id)
            return episode

    def delete_episode(self, episode_id: int) -> None:
        with self._session_factory() as session:
            episode: Episode = session.query(Episode).filter(Episode.id == episode_id).first()
            if episode is None:
                raise NotFoundError("episode",  "id", episode_id)
            episode.delete(episode)
            session.commit()
        

    
