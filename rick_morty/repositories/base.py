from typing import Callable

class BaseRepository:

    def __init__(self, session_factory: Callable):
        self._session_factory = session_factory
