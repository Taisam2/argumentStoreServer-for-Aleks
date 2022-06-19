from typing import List
from fastapi import APIRouter, HTTPException

from argument_store.config.db import DatabaseClient
from argument_store.models.argument.argument import Argument

from argument_store.schemas.argument import argumentsEntity

from fastapi.encoders import jsonable_encoder

argument = APIRouter()

client = DatabaseClient()

@argument.get('/getArguments')
async def findAllArguments():
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        argument_collection = client.get_argument_collection()
        response: List = argumentsEntity(argument_collection.find(session=session))
        if not response:
            raise HTTPException(status_code=404, detail="Keine Argumente gespeichert.")
        else:
            return response

@argument.post('/addArgument')
async def createArgument(argument: Argument):
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        argument_collection = client.get_argument_collection()
        allArguments: List = argumentsEntity(argument_collection.find())
        for args in allArguments:
            if args['description'] == argument.description:
                raise HTTPException(status_code=409, detail="Argument ist bereits vorhanden.")
        with session.start_transaction():
            argument_collection.insert_one(jsonable_encoder(argument))       
        return "Argument erfolgreich hinzugefügt!"