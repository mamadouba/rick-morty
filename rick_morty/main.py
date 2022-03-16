#!/bin/python3

import logging
from fastapi import FastAPI
from rick_morty.endpoints import characters
from rick_morty.endpoints import episodes 
from rick_morty.endpoints import comments
from rick_morty.scripts import db

def create_app() -> FastAPI:

    app = FastAPI()
    app.include_router(characters.router)
    app.include_router(episodes.router)
    app.include_router(comments.router)

    @app.get("/")
    def root():
        return {
            "message": "Rick & Morty API"
        }
    
    return app
    
app = create_app()