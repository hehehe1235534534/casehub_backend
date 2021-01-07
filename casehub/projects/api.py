from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_projects():
    return {"message": "Hello World"}


@router.get("/{id}")
async def get_project():
    return {"message": "Hello World"}


@router.post("/")
async def create_project():
    return {"message": "Hello World"}


@router.put("/{id}")
async def update_project():
    return {"message": "Hello World"}


@router.delete("/{id}")
async def delete_project():
    return {"message": "Hello World"}