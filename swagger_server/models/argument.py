from datetime import datetime
from pydantic import BaseModel

class Argument(BaseModel):
    date: datetime
    text: str
    author: str
    approval: str
    links: str
    linkedArguments: str