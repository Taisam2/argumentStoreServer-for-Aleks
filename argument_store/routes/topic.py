from bson import ObjectId
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
import requests

from argument_store.models.topic import Topic
from argument_store.config.db import conn
from argument_store.schemas.topic import topicsEntity

topic = APIRouter() 

@topic.get('/getTopics')
async def findAllTopics():
    if not conn.ArgumentStore.local.topic.find():
        raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
    response: List = topicsEntity(conn.ArgumentStore.local.topic.find())
    if response == []:
        raise HTTPException(status_code=404, detail="Keine Themen gespeichert.")
    else:
        return response

@topic.get('/findById')
async def findTopicById(searchedId: str):
    if not conn.ArgumentStore.local.topic.find({ "_id": ObjectId(searchedId)}):
        raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
    else: 
        topic: Topic = topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(searchedId)}))
    if not topic:
        raise HTTPException(status_code=204, detail="Keine Themen mit der ID: " + searchedId + " gespeichert.")
    else:
        return topic

@topic.post('/addTopic')
async def createTopic(topic: Topic):
    if not conn.ArgumentStore.local.topic.find():
        raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
    else:
        topicsFromDb: List = topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(topic.id)}))
    if topicsFromDb[0]['title'] == topic.title:
        raise HTTPException(status_code=409, detail="Thema ist bereits vorhanden.")
    else:
        conn.ArgumentStore.local.topic.insert_one(jsonable_encoder(topic))
    return "Thema erfolgreich hinzugefügt!"
    
@topic.post('/addSolutionOption')
async def addSolutionToArray(topic: Topic):
    if not conn.ArgumentStore.local.topic.find():
        raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
    else:
        topicsFromDb: List = topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(topic.id)}))
    for solutions in topicsFromDb[0]['solutionOption']:
        if solutions == topic.solutionOption[0]:
            raise HTTPException(status_code=409, detail="Lösungsvorschlag ist bereits vorhanden.")
    else:
        conn.ArgumentStore.local.topic.update_one({ "_id": ObjectId(topic.id)}, { '$push': {"solutionOption":{ "$each": topic.solutionOption} }})        
    return "Lösungsvorschlag erfolgreich zum Thema hinzugefügt!"    