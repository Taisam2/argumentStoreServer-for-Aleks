from typing import List
import requests
from typing_extensions import Self
from urllib.error import HTTPError
from fastapi import APIRouter, HTTPException, status

from argument_store.config.db import conn
from argument_store.models.argument import Argument
from argument_store.schemas.argument import argumentsEntity

from fastapi.encoders import jsonable_encoder

argument = APIRouter()


@argument.get('/getArguments')
async def findAllArguments():
    try:
        if not conn.ArgumentStore.local.argument.find():
            raise HTTPException(status_code=444, detail="Verbindung zur Datenbank unterbrochen.")
        response: List = argumentsEntity(conn.ArgumentStore.local.argument.find())
        if not response:
            #raise HTTPError(code=404, msg="Keine Argumente gespeichert.", url="", hdrs="" , fp="")
            raise HTTPException(status_code=404, detail="Keine Argumente gespeichert.")
        else:
            return response
    except requests.HTTPError as err:
        return {"code": err.status}
    except Exception as err:
        print("Hier")

@argument.post('/addArgument')
async def createArgument(argument: Argument):
    try:
        conn.ArgumentStore.local.argument.insert_one(jsonable_encoder(argument))
        return "Argument erfolgreich hinzugefügt!"
    except Exception as e:
        print("Error in /addArgument route: " + e)

    


