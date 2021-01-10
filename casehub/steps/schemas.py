import enum
from pydantic import BaseModel


class StepType(str, enum.Enum):
    precondition = 'precondition'
    body = 'body'
    result = 'result'


class StepSchema(BaseModel):
    name: str
    text: str
    type: StepType
    place: int
    case_id: int
