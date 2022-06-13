from pydantic import BaseModel

from argument_store.models.ArgumentOptionEnum import ArgumentOptionEnum

class ArgumentOption(BaseModel):
    option: ArgumentOptionEnum