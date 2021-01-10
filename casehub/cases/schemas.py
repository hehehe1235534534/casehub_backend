from typing import Optional

from pydantic import BaseModel


class CaseSchema(BaseModel):
    name: str
    description: Optional[str]
    suite_id: int
