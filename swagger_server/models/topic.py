from pydantic import BaseModel

class Topic(BaseModel):
    title: str
    solutionOption: list[str] = []

