from fastapi import APIRouter

from casehub.steps.models import StepModel
from casehub.steps.schemas import StepSchema

router = APIRouter(prefix='/steps', tags=['Steps'])


@router.get("/")
async def get_steps():
    steps = await StepModel.all()
    return steps


@router.get("/{id}", response_model=StepSchema)
async def get_step():
    step_model = await StepModel.get_or_404(id)
    return step_model.to_dict()


@router.post("/")
async def create_step(step: StepSchema):
    data = await StepModel.create(
        name=step.name,
        text=step.text,
        type=step.type,
        place=step.place
    )
    return data.to_dict()


@router.put("/{id}")
async def update_step():
    return {"message": "Hello World"}


@router.delete("/{id}")
async def delete_step():
    return {"message": "Hello World"}
