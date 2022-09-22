from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Rating(BaseModel):
    topicId: str
    optionNumber: int
    optionName: str
    sol_rat_1: float
    sol_rat_2: float
    sol_rat_3: float    
    date: Optional[datetime] = datetime.now().strftime("%d:%m:%Y %H:%M:%S")