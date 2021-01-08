from fastapi import FastAPI
from gino import Gino

from casehub.projects.api import router as projects_router


def get_app():
    db = Gino()
    app = FastAPI(title='Casehub')
    app.include_router(projects_router, prefix='/projects')
    return app
