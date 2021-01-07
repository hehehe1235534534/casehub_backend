from fastapi import FastAPI
from projects.api import router as projects_router


app = FastAPI(title='Casehub')
app.include_router(projects_router, prefix='/projects')
