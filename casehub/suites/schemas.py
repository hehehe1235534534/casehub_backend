from pydantic import BaseModel


class SuiteSchema(BaseModel):
    name: str
    project_id: int
