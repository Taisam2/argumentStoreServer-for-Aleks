from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException

from argument_store.config.db import DatabaseClient
from argument_store.models.argument.argument import Argument

from argument_store.schemas.argument import argumentsEntity

from fastapi.encoders import jsonable_encoder

argument = APIRouter()

client = DatabaseClient()
database_client = client.create_database_client()

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
        argument_collection = database_client.get_argument_collection()
        allArguments: List = argumentsEntity(argument_collection.find())
        for args in allArguments:
            if args['description'] == argument.description:
                raise HTTPException(status_code=409, detail="Argument ist bereits vorhanden.")
        with session.start_transaction():
            argument_collection.insert_one(jsonable_encoder(argument))  
            session.commit_transaction()     
            session.end_session()     
        return "Argument erfolgreich hinzugefügt!"

@argument.get('/findArgumentById/{searchedId}')
async def findArugmentById(searchedId: str):
    with database_client.start_session() as session:
        argument_collection = client.get_argument_collection()
        argument: Argument = argumentsEntity(argument_collection.find({ "_id": ObjectId(searchedId)}))
        if not argument:
            raise HTTPException(status_code=204, detail="Kein Argument mit der ID: " + searchedId + " vorhanden.")
        else:
            return argument