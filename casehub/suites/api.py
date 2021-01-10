from fastapi import APIRouter

from casehub.suites.models import SuiteModel
from casehub.suites.schemas import SuiteSchema

router = APIRouter(prefix='/suites', tags=['Suites'])


@router.get("/")
async def get_suites():
    suites = await SuiteModel.all()
    return suites


@router.get("/{id}", response_model=SuiteSchema)
async def get_suite():
    suite_model = await SuiteModel.get_or_404(id)
    return suite_model.to_dict()


@router.post("/")
async def create_suite(suite: SuiteSchema):
    data = await SuiteModel.create(
        name=suite.name,
        project_id=suite.project_id
    )
    return data.to_dict()


@router.put("/{id}")
async def update_suite():
    return {"message": "Hello World"}


@router.delete("/{id}")
async def delete_suite():
    return {"message": "Hello World"}