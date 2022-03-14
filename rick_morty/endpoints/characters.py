from typing import List
from fastapi import APIRouter, Depends
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas 

router = APIRouter(prefix="/characters", tags=["characters"])
    
@router.get("/", responses={
    200: {"model": List[schemas.CharacterOut]},
    404: {"model": schemas.Message }})
def get_characters(repository: Repository = Depends(get_repository)):
    return repository.get_characters()
