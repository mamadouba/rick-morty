from pydantic import BaseModel

from .characters import *
from .episodes import *
from .comments import *
from .users import *


class Message(BaseModel):
    message: str
