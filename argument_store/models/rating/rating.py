from datetime import datetime
from xmlrpc.client import boolean
from pydantic import BaseModel
from typing import Union

class Rating(BaseModel):
    optionNumber: int
    optionName: str
    username: str
    sol_rat_1: float
    sol_rat_2: float
    sol_rat_3: Union[boolean, None] = False
    date: Union[datetime, None] = datetime.now().strftime("%d:%m:%Y %H:%M:%S")