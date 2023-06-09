from datetime import datetime
from xmlrpc.client import boolean
from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime

class Rating(BaseModel):
    optionNumber: int
    optionName: str
    username: str
    sol_rat_1: float
    sol_rat_2: float
    sol_rat_3: Union[boolean, None] = False
    date: datetime = Field(default_factory=datetime.utcnow)