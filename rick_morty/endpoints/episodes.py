from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas

router = APIRouter(prefix="/episodes", tags=["episodes"])
    
@router.get("/", responses={200: {"model": List[schemas.EpisodeOut]}})
def get_episodes(page: int = 1, per_page: int = 10, filters: str = "", repository: Repository = Depends(get_repository)):
    episodes = repository.get_episodes(page, per_page, filters)
    return JSONResponse(status_code=200, content=episodes)