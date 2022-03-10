import logging
from fastapi import FastAPI

logger = logging.getLogger(__name__)

def create_app() -> FastAPI:

    logger.debug("create-app")

    app = FastAPI()

    @app.get("/")
    def root():
        return {
            "name": "Rick & Morty"
        }
    return app
    
app = create_app()