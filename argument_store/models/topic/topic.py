from typing import Optional
from bson import List
from pydantic import BaseModel

from argument_store.models.topic.topicSolutionOption import TopicSolutionOption

class Topic(BaseModel):
    id: Optional[str] = None
    title: str
    solutionOption: List[TopicSolutionOption] = []

