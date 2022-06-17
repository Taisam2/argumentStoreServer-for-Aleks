from bson import ObjectId
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
import requests

from argument_store.models.Topic import Topic
from argument_store.config.db import conn
from argument_store.schemas.topic import topicEntity, topicsEntity

topic = APIRouter() 

@topic.get('/getTopics')
async def findAllTopics():
    try:
        if not conn.ArgumentStore.local.topic.find():
            raise HTTPException(status_code=444, detail="Verbindung zur Datenbank unterbrochen.")
        response: List = topicsEntity(conn.ArgumentStore.local.topic.find())
        if response == []:
             raise HTTPException(status_code=204, detail="Keine Themen gespeichert.")
        else:
            return response
    except requests.HTTPError as err:
        return {"code": err.status}

@topic.get('/findById')
async def findTopicById(searchedId: str):
    try:
        if not conn.ArgumentStore.local.topic.find({ "_id": ObjectId(searchedId)}):
            raise HTTPException(status_code=444, detail="Verbindung zur Datenbank unterbrochen.")
        else: 
            topic: Topic = topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(searchedId)}))
        if not topic:
            raise HTTPException(status_code=204, detail="Keine Themen mit der ID: " + searchedId + " gespeichert.")
        else:
            return topic
    except requests.HTTPError as err:
        return {"code": err.status}

@topic.post('/addTopic')
async def createTopic(topic: Topic):
    try:
        if not conn.ArgumentStore.local.topic.find():
            raise HTTPException(status_code=444, detail="Verbindung zur Datenbank unterbrochen.")
        else:
            topicsFromDb: List = topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(topic.id)}))
        if topicsFromDb[0]['title'] == topic.title:
            raise HTTPException(status_code=409, detail="Thema ist bereits vorhanden.")
        else:
            conn.ArgumentStore.local.topic.insert_one(jsonable_encoder(topic))
        return "Thema erfolgreich hinzugefügt!"
    except requests.HTTPError as err:
        return {"code": err.status} 

@topic.post('/addSolutionOption')
async def addSolutionToArray(topic: Topic):
    try:
        if not conn.ArgumentStore.local.topic.find():
            raise HTTPException(status_code=444, detail="Verbindung zur Datenbank unterbrochen.")
        else:
            topicsFromDb: List = topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(topic.id)}))
        for solutions in topicsFromDb[0]['solutionOption']:
            if solutions == topic.solutionOption[0]:
                raise HTTPException(status_code=409, detail="Lösungsvorschlag ist bereits vorhanden.")
        else:
            conn.ArgumentStore.local.topic.update_one({ "_id": ObjectId(topic.id)}, { '$push': {"solutionOption":{ "$each": topic.solutionOption} }})        
        return "Lösungsvorschlag erfolgreich zum Thema hinzugefügt!"
    except requests.HTTPError as err:
        return {"code": err.status} 
    