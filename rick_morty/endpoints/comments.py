from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas

router = APIRouter(prefix="/comments", tags=["comments"])
    
@router.get("/", responses={
    200: {"model": List[schemas.CommentOut]},
    404: {"model": schemas.Message }})
def get_comments(page: int = 1, per_page: int = 10, filters: str = "", repository: Repository = Depends(get_repository)):
    return repository.get_comments(page, per_page, filters)

@router.post("/", responses={
    201: {"model": schemas.CommentOut},
    400: {"model": schemas.Message },
    404: {"model": schemas.Message }})
def create_comment(data: schemas.CommentIn, repository: Repository = Depends(get_repository)):
    data_keys = ["episode_id", "character_id"]
    if not any([True for k in data_keys if k in data.dict()]):
        message = "episode_id or character_id should be provided"
        return JSONResponse(status_code=400, content={"message": message})
    
    if data.episode_id:
        episode = repository.get_episode(data.episode_id)
        if not episode:
            return JSONResponse(status_code=404, content={"message": f"episode {data.episode_id} not found"})
        if data.character_id:
            if data.character_id not in episode.get("characters"):
                return JSONResponse(status_code=400, content={"message": "episode and character are not associated"})
    if data.character_id:
        character = repository.get_character(data.character_id)
        if not character:
            return JSONResponse(status_code=404, content={"message": f"character {data.character_id} not found"})
    return repository.create_comment(**data.dict())

@router.get("/{comment_id}", responses={
    200: {"model": schemas.CommentOut},
    404: {"model": schemas.Message }})
def get_comment(comment_id: int, repository: Repository = Depends(get_repository)):
    comment = repository.get_comment(comment_id)
    if not comment:
        return JSONResponse(status_code=404, content={"message": f"comment {comment_id} not found"})
    return comment

@router.delete("/{comment_id}", responses={
    200: {"model": schemas.Message},
    404: {"model": schemas.Message }})
def delete_comment(comment_id: int, repository: Repository = Depends(get_repository)):
    if repository.delete_comment(comment_id):
        return JSONResponse(status_code=200, content={"message": f"comment {comment_id} deleted"})
    return JSONResponse(status_code=404, content={"message": f"comment {comment_id} not found"})
