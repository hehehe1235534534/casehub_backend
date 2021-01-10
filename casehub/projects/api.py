from fastapi import APIRouter

from casehub.projects.models import ProjectModel
from casehub.projects.schemas import ProjectSchema

router = APIRouter(prefix='/projects', tags=['Projects'])


@router.get("/")
async def get_projects():
    projects = await ProjectModel.all()
    return projects


@router.get("/{id}")
async def get_project():
    project_model = await ProjectModel.get_or_404(id)
    return project_model.to_dict()


@router.post("/")
async def create_project(project: ProjectSchema):
    data = await ProjectModel.create(name=project.name)
    return data.to_dict()


@router.put("/{id}")
async def update_project():
    return {"message": "Hello World"}


@router.delete("/{id}")
async def delete_project():
    return {"message": "Hello World"}