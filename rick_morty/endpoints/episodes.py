from typing import List
from fastapi import APIRouter, Depends
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas

router = APIRouter(prefix="/episodes", tags=["episodes"])
    
@router.get("/", responses={
    200: {"model": List[schemas.EpisodeOut]},
    404: {"model": schemas.Message }})
def get_episodes(repository: Repository = Depends(get_repository)):
    return repository.get_episodes()
