#!/bin/python3
import rick_morty
import uvicorn
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
        return {
            "message": "Rick & Morty API"
        }
    
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("rick_morty.main:create_app()", hots="0.0.0.0", port=8000, reload=True)