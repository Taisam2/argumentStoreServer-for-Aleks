from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Argument(BaseModel):
    topicId: str
    argumentOption: str
    solutionOption: str
    description: str
    date: Optional[str] = datetime.now().strftime("%d:%m:%Y %H:%M:%S")
    author: str
    approval: str
    links: str
    linkedArguments: str