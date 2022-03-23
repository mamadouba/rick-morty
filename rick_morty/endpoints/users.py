import bcrypt
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from rick_morty.repositories import Repository
from rick_morty.dependencies import get_repository
from rick_morty import schemas
from rick_morty.auth import auth

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/logout", dependencies=[Depends(auth.JWTBearer())])
def logout(request: Request):
    from rick_morty.main import revoked_tokens

    tuid = request.state.user.get("tuid")
    expires = request.state.user.get("expires")
    revoked_tokens[tuid] = expires
    return JSONResponse(status_code=200, content={"message": "successfully logged out"})


@router.post("/login", responses={200: {"model": schemas.Login}})
def login(data: schemas.Login, repository: Repository = Depends(get_repository)):
    user = repository.find_user(data.email)
    if not user:
        return JSONResponse(status_code=401, content={"message": "Invalid credentials"})
    if not bcrypt.checkpw(data.password.encode(), user.get("password_hash")):
        return JSONResponse(status_code=401, content={"message": "Invalid credentials"})
    token = auth.sign_jwt(**user)
    return JSONResponse(status_code=200, content=token)


@router.get(
    "/",
    responses={200: {"model": schemas.UserList}},
    dependencies=[Depends(auth.JWTBearer())],
)
def get_users(
    page: int = 1,
    per_page: int = 10,
    filters: str = "",
    repository: Repository = Depends(get_repository),
):
    users = repository.get_users(page, per_page, filters)
    return JSONResponse(status_code=200, content=users)


@router.post(
    "/",
    responses={
        201: {"model": schemas.UserOut},
        400: {"model": schemas.Message},
        404: {"model": schemas.Message},
    },
)
def create_user(data: schemas.UserIn, repository: Repository = Depends(get_repository)):

    if repository.find_user(data.email):
        return JSONResponse(
            status_code=409, content={"message": f"User '{data.email}' already exist"}
        )
    try:
        payload = data.dict()
        password = payload.pop("password")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode(), salt)
        payload["password_hash"] = password_hash
        user = repository.create_user(**payload)
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": str(exc)})
    return JSONResponse(status_code=201, content=user)


@router.get(
    "/{user_id}",
    responses={200: {"model": schemas.UserOut}, 404: {"model": schemas.Message}},
    dependencies=[Depends(auth.JWTBearer())],
)
def get_user(user_id: int, repository: Repository = Depends(get_repository)):
    user = repository.get_user(user_id)
    if not user:
        return JSONResponse(
            status_code=404, content={"message": f"user {user_id} not found"}
        )
    return JSONResponse(status_code=200, content=user)


@router.delete(
    "/{user_id}",
    responses={200: {"model": schemas.UserOut}, 404: {"model": schemas.Message}},
    dependencies=[Depends(auth.JWTBearer())],
)
def delete_user(user_id: int, repository: Repository = Depends(get_repository)):
    user = repository.delete_user(user_id)
    if not user:
        return JSONResponse(
            status_code=404, content={"message": f"user {user_id} not found"}
        )
    return JSONResponse(status_code=200, content={"message": "successfully deleted"})
