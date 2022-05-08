from fastapi import APIRouter
from config.db import conn, result
from models.argument import Argument
from schemas.argument import argumentsEntity

from fastapi.encoders import jsonable_encoder

argument = APIRouter()


@argument.get('/getArguments')
async def findAllArguments():
    return argumentsEntity(conn.local.argument.find())

@argument.post('/addArgument')
async def createArgument(argument: Argument):
    json_compatible_argument = jsonable_encoder(argument)
    conn.local.argument.insert_one(json_compatible_argument)
    return "Successful added a Argument!"


