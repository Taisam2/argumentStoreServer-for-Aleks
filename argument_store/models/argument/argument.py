from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from argument_store.models.argument.argumentOptionEnum import ArgumentOptionEnum
from argument_store.models.topic.topicSolutionOption import TopicSolutionOption


class Argument(BaseModel):
    topicId: str
    argumentOption: ArgumentOptionEnum
    solutionOption: TopicSolutionOption
    description: str
    date: Optional[datetime] = datetime.now().strftime("%d:%m:%Y %H:%M:%S")
    author: str
    approval: str
    links: str
    linkedArguments: str



print(Argument.schema_json(indent=2))