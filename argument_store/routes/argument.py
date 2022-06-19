from typing import List
from fastapi import APIRouter, HTTPException
from argument_store.config.db import conn
from argument_store.models.argument.argument import Argument
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
        print("Error in /getArguments route: " )

@argument.post('/addArgument')
async def createArgument(argument: Argument):
    if not conn.ArgumentStore.local.argument.find():
        raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
    else:
        allArguments: List = argumentsEntity(conn.ArgumentStore.local.argument.find())
    for args in allArguments:
        if args['description'] == argument.description:
            raise HTTPException(status_code=409, detail="Argument ist bereits vorhanden.")
    conn.ArgumentStore.local.argument.insert_one(jsonable_encoder(argument))       
    return "Argument erfolgreich hinzugefügt!"

    


