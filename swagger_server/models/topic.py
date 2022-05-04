import numbers
from typing import Optional
from pydantic import BaseModel

class Topic(BaseModel):
    id: Optional[str] = None
    title: str
    solutionOption: list[str] = []

