from typing import List
from fastapi import APIRouter
from config.db import conn
from models.argument import Argument
from schemas.argument import argumentsEntity

from fastapi.encoders import jsonable_encoder

argument = APIRouter()


@argument.get('/getArguments')
async def findAllArguments():
    try:
        response: List = argumentsEntity(conn.ArgumentStore.local.argument.find())
        if not response:
            return "Bisher sind keine Argumente gespeichert."
        else:
            return response
    except Exception as e:
        print("Error in /getArguments route: " + e)

@argument.post('/addArgument')
async def createArgument(argument: Argument):
    try:
        conn.ArgumentStore.local.argument.insert_one(jsonable_encoder(argument))
        return "Argument erfolgreich hinzugefügt!"
    except Exception as e:
        print("Error in /addArgument route: " + e)

    


