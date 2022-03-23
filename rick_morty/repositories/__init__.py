from typing import Callable
from .users import UserRepository
from .episodes import EpisodeRepository
from .characters import CharacterRepository
from .episodes import EpisodeRepository
from .comments import CommentRepository


class Repository(
    UserRepository, EpisodeRepository, CharacterRepository, CommentRepository
):
    def __init__(self, session_factory: Callable) -> None:
        UserRepository.__init__(self, session_factory)
        EpisodeRepository.__init__(self, session_factory)
        CharacterRepository.__init__(self, session_factory)
        CommentRepository.__init__(self, session_factory)
