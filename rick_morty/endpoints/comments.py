from importlib.resources import contents
from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, FileResponse
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas
from rick_morty.auth import auth

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("/export", status_code=200, dependencies=[Depends(auth.JWTBearer())])
def export_comments(repository: Repository = Depends(get_repository)):
    comments = repository.export_comments()
    with open("comments.csv", "w") as fd:
        fd.write("id;episode_id,character_id;comment\n")
        for comment in comments:
            row = "{};{};{};{}".format(
                comment.get("id"),
                comment.get("episode_id"),
                comment.get("character_id"),
                comment.get("comment"),
            )
            fd.write(f"{row}\n")
    return FileResponse(
        path="comments.csv", filename="comments.csv", media_type="text/csv"
    )


@router.get(
    "/",
    responses={200: {"model": schemas.CommentList}},
    dependencies=[Depends(auth.JWTBearer())],
)
def get_comments(
    page: int = 1,
    per_page: int = 10,
    filters: str = "",
    repository: Repository = Depends(get_repository),
):
    comments = repository.get_comments(page, per_page, filters)
    return JSONResponse(status_code=200, content=comments)


@router.post(
    "/",
    responses={
        201: {"model": schemas.CommentOut},
        400: {"model": schemas.Message},
        404: {"model": schemas.Message},
    },
    dependencies=[Depends(auth.JWTBearer())],
)
def create_comment(
    data: schemas.CommentIn, repository: Repository = Depends(get_repository)
):
    data_keys = ["episode_id", "character_id"]
    if not any([True for k in data_keys if k in data.dict()]):
        message = "episode_id or character_id should be provided"
        return JSONResponse(status_code=400, content={"detail": message})

    if data.episode_id:
        episode = repository.get_episode(data.episode_id)
        if not episode:
            return JSONResponse(
                status_code=404,
                content={"detail": f"episode {data.episode_id} not found"},
            )
        if data.character_id:
            if data.character_id not in episode.get("characters"):
                return JSONResponse(
                    status_code=400,
                    content={"detail": "episode and character are not associated"},
                )

    if data.character_id:
        character = repository.get_character(data.character_id)
        if not character:
            return JSONResponse(
                status_code=404,
                content={"detail": f"character {data.character_id} not found"},
            )

    try:
        comment = repository.create_comment(**data.dict())
    except Exception as exc:
        return JSONResponse(status_code=500, content={"detail": str(exc)})
    return JSONResponse(status_code=201, content=comment)


@router.get(
    "/{comment_id}",
    responses={200: {"model": schemas.CommentOut}, 404: {"model": schemas.Message}},
    dependencies=[Depends(auth.JWTBearer())],
)
def get_comment(comment_id: int, repository: Repository = Depends(get_repository)):
    comment = repository.get_comment(comment_id)
    if not comment:
        return JSONResponse(
            status_code=404, content={"detail": f"comment {comment_id} not found"}
        )
    return JSONResponse(status_code=200, content=comment)


@router.delete(
    "/{comment_id}",
    responses={200: {"model": schemas.CommentOut}, 404: {"model": schemas.Message}},
    dependencies=[Depends(auth.JWTBearer())],
)
def delete_comment(comment_id: int, repository: Repository = Depends(get_repository)):
    comment = repository.delete_comment(comment_id)
    if not comment:
        return JSONResponse(
            status_code=404, content={"detail": f"comment {comment_id} not found"}
        )
    return JSONResponse(status_code=200, content={"detail": "successfully deleted"})
