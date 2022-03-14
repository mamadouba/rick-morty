from typing import Callable
from .users import UserRepository 
from .episodes import EpisodeRepository
from .characters import CharacterRepository
from .episodes import EpisodeRepository
from .comments import CommentRepository
from .episodecaracters import EpisodecaracterRepository

class Repository(
    UserRepository,
    EpisodeRepository,
    CharacterRepository,
    CommentRepository,
    EpisodecaracterRepository):
    
    def __init__(self, session_factory: Callable) -> None:
        UserRepository.__init__(self, session_factory)
        EpisodeRepository.__init__(self, session_factory)
        CharacterRepository.__init__(self, session_factory)
        CommentRepository.__init__(self, session_factory)
        EpisodecaracterRepository.__init__(self, session_factory)

