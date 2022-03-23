#!/bin/python3
from fastapi import FastAPI
from rick_morty.endpoints import characters
from rick_morty.endpoints import episodes
from rick_morty.endpoints import comments
from rick_morty.endpoints import users
from rick_morty.scripts import db
from rick_morty.auth import auth

revoked_tokens: dict = {}


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(characters.router)
    app.include_router(episodes.router)
    app.include_router(comments.router)
    app.include_router(users.router)

    @app.get("/")
    def root():
        return {"detail": "Rick & Morty API"}

    return app


app = create_app()
