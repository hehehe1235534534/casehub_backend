import logging

from fastapi import FastAPI

from casehub.projects.api import router as projects_router
from casehub.steps.api import router as steps_router
from casehub.suites.api import router as suites_router
from casehub.cases.api import router as cases_router
from .db import db

logger = logging.getLogger(__name__)


def get_app():
    app = FastAPI(title='Casehub')
    app.include_router(projects_router, prefix='/projects')
    app.include_router(steps_router, prefix='/steps')
    app.include_router(suites_router, prefix='/suites')
    app.include_router(cases_router, prefix='/cases')
    db.init_app(app)
    return app
