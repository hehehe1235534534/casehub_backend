import logging

from fastapi import FastAPI

from casehub.projects.api import router as projects_router
from .db import db

logger = logging.getLogger(__name__)


def get_app():
    app = FastAPI(title='Casehub')
    app.include_router(projects_router, prefix='/projects')
    db.init_app(app)
    return app
