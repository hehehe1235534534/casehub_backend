from fastapi import FastAPI

from casehub.projects.api import router as projects_router
from .db import db


def get_app():
    app = FastAPI(title='Casehub')
    app.include_router(projects_router, prefix='/projects')
    db.init_app(app)
    return app
