#!/bin/python3

import logging
from fastapi import FastAPI
from rick_morty.endpoints import characters
from rick_morty.endpoints import episodes 
from rick_morty.endpoints import comments

logger = logging.getLogger(__name__)

def create_app() -> FastAPI:

    logger.debug("create-app")

    app = FastAPI()
    app.include_router(characters.router)
    app.include_router(episodes.router)
    app.include_router(comments.router)

    @app.get("/")
    def root():
        return {
            "name": "Rick & Morty"
        }
    return app
    
app = create_app()