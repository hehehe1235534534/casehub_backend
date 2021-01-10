from fastapi import APIRouter

from casehub.cases.models import CaseModel
from casehub.cases.schemas import CaseSchema

router = APIRouter(prefix='/cases', tags=['Cases'])


@router.get("/")
async def get_cases():
    cases = await CaseModel.all()
    return cases


@router.get("/{id}", response_model=CaseSchema)
async def get_case():
    case_model = await CaseModel.get_or_404(id)
    return case_model.to_dict()


@router.post("/")
async def create_case(case: CaseSchema):
    data = await CaseModel.create(
        name=case.name,
        description=case.description,
        suite_id=case.suite_id
    )
    return data.to_dict()


@router.put("/{id}")
async def update_case():
    return {"message": "Hello World"}


@router.delete("/{id}")
async def delete_case():
    return {"message": "Hello World"}