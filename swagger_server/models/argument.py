from datetime import datetime
from pydantic import BaseModel


class Argument(BaseModel):
    topicId: str
    argumentOption: str
    solutionOption: str
    description: str
    date: str
    author: str
    approval: str
    links: str
    linkedArguments: str