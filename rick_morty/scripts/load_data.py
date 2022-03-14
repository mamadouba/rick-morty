import os
import json
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository

def read_data(path: str) -> dict:
    """
    Reads file content
    args: 
        path: filename
    returns: dict of data
    """
    if os.path.exists(path):
        raise Exception(f"File {path} not found")
    with open(path, "r") as fd:
        data = json.loads(fd.read())
    return data

def load_episodes(path: str, repository: Repository) -> None:
    """
    Loads episodes data from file to database
    args: 
        path: data filename
        repository: repository instance
    """
    for episode in read_data(path):
        repository.create_episode(**episode)

def load_characters(path: str, repository: Repository) -> None:
    """
    Loads characters data from file to database
    args: 
        path: data filename
        repository: repository instance
    """

    for character in read_data(path):
        repository.create_character(**character)

if __name__ == "__main__":
    repository: Repository = get_repository()
    load_episodes("data/episodes.json", repository)
    load_characters("data/characters.json", repository)
