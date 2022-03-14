from typing import List, Callable
from rick_morty.database.models import Episodecaracter
from .base import BaseRepository

class EpisodecaracterRepository(BaseRepository):

    def create_episodecaracter(self, episode_id: int, character_id: int) -> Episodecaracter:
        episodecaracter = Episodecaracter(
            episode_id = episode_id,
            character_id = character_id
        )
        
        with self._session_factory() as session:
            session.add(episodecaracter)
            session.commit()
            session.refresh(episodecaracter)
            return episodecaracter
    
    def get_episodecaracters(self) -> List[Episodecaracter]:
        with self._session_factory() as session:
            return session.query(Episodecaracter).all()
    
