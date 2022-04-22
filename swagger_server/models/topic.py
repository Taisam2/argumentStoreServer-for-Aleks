import datetime
from pydantic import BaseModel
from models.argument import Argument
from typing import Optional, List

class Topic(BaseModel):
    title: str
    argument: Optional[List[Argument]]