from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas 

router = APIRouter(prefix="/characters", tags=["characters"])
    
@router.get("/", responses={200: {"model": schemas.CharacterList}})
def get_characters(page: int = 1, per_page: int = 10, filters: str = "", repository: Repository = Depends(get_repository)):
    characters =  repository.get_characters(page, per_page, filters)
    return JSONResponse(status_code=200, content=characters)