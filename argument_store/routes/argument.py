from typing import List
from fastapi import APIRouter
from argument_store.config.db import conn
from argument_store.models.Argument import Argument
from argument_store.models.ArgumentOptionEnum import ArgumentOptionEnum
from argument_store.schemas.argument import argumentsEntity

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
        for option in ArgumentOptionEnum:
            if option == argument.argumentOption:
                print("option: " + option + "\nArgumentoption: " + argument.argumentOption)
        #conn.ArgumentStore.local.argument.insert_one(jsonable_encoder(argument))
        return "Argument erfolgreich hinzugefügt!"
    except Exception as e:
        print("Error in /addArgument route: " + e)

    


