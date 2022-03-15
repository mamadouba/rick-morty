#!/bin/env python3
import os
import json
import logging

from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository, get_db
from rick_morty.schemas import CharacterIn
from rick_morty.schemas import EpisodeIn

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
        model = CharacterIn(**character)
        repository.create_character(model.dict(exclude={"episode"}))
    

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
        repository.create_episode(model.dict())

def main():
    db = get_db()
    db.create_database()
    repository: Repository = get_repository()
    load_characters("data/characters.json", repository)
    load_episodes("data/episodes.json", repository)

if __name__ == "__main__":
    main()