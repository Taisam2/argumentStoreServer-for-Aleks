import datetime
from pydantic import BaseModel
from models.argument import Argument

class Topic(BaseModel):
    title: str
    argument: Argument