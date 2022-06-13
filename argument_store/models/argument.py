from datetime import datetime
from pydantic import BaseModel

from argument_store.models.ArgumentOption import ArgumentOption
from argument_store.models.ArgumentOptionEnum import ArgumentOptionEnum


class Argument(BaseModel):
    topicId: str
    argumentOption: ArgumentOptionEnum
    solutionOption: str
    description: str
    date: datetime = datetime.now().strftime("%d:%m:%Y %H:%M:%S")
    author: str
    approval: str
    links: str
    linkedArguments: str