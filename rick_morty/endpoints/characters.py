from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas 

router = APIRouter(prefix="/characters", tags=["characters"])
    
@router.get("/", responses={200: {"model": List[schemas.CharacterOut]}})
def get_characters(repository: Repository = Depends(get_repository)):
    characters = repository.get_characters()
    return JSONResponse(status_code=200, content=characters)
