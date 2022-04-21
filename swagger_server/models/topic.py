import datetime
from pydantic import BaseModel
from swagger_server.models.argument import Argument

class Topic(BaseModel):
    title: str
    argument: Argument