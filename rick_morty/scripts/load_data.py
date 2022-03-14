import os
import json
import logging

from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository, get_db
from rick_morty.schemas.characters import CharacterIn
from rick_morty.schemas.episodes import EpisodeIn

logger = logging.getLogger(__name__)

def read_data(path: str) -> dict:
    """
    Reads file content
    args: 
        path: filename
    returns: dict of data
    """
    logger.debug(f"load data from {path}")
    if not os.path.exists(path):
        raise Exception(f"File {path} not found")
    with open(path, "r") as fd:
        data = json.loads(fd.read())
    return data

def load_characters(path: str, repository: Repository) -> None:
    """
    Loads characters data from file to database
    args: 
        path: data filename
        repository: repository instance
    """

    for character in read_data(path):
        logger.debug(f"create character {character['name']}")
        data = CharacterIn(**character)
        repository.create_character(data.dict(exclude={"episode"}))
    

def load_episodes(path: str, repository: Repository) -> None:
    """
    Loads episodes data from file to database
    args: 
        path: data filename
        repository: repository instance
    """
    for episode in read_data(path):
        logger.debug(f"create episode {episode['name']}")
        model = EpisodeIn(**episode)
        
        data = model.dict()

        data["characters"] = []
        for character_id in model.characters:
            character = repository.get_character(character_id)
            if character != None:
                data["characters"].append(character)
        repository.create_episode(data)


if __name__ == "__main__":
    db = get_db()
    db.create_database()
    repository: Repository = get_repository()
    load_characters("data/characters.json", repository)
    load_episodes("data/episodes.json", repository)
