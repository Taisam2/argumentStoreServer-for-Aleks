from bson import ObjectId
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from argument_store.models.topic import Topic
from argument_store.config.db import DatabaseClient
from argument_store.schemas.topic import topicsEntity

topic = APIRouter() 

client = DatabaseClient()
database_client = client.create_database_client()

@topic.get('/getTopics')
async def findAllTopics():
    topic_collection = client.get_topic_collection()
    response: List = topicsEntity(topic_collection.find())
    if response == []:
        raise HTTPException(status_code=404, detail="Keine Themen gespeichert.")
    else:
        return response

@topic.get('/findById')
async def findTopicById(searchedId: str):
    with database_client.start_session() as session:
        topic_collection = client.get_topic_collection()
        topic: Topic = topicsEntity(topic_collection.find({ "_id": ObjectId(searchedId)}))
        if not topic:
            raise HTTPException(status_code=204, detail="Keine Themen mit der ID: " + searchedId + " gespeichert.")
        else:
            return topic

@topic.post('/addTopic')
async def createTopic(topic: Topic):
    with database_client.start_session() as session:
        topic_collection = client.get_topic_collection()
        topicsFromDb: List = topicsEntity(topic_collection.find({ "_id": ObjectId(topic.id)}))
        if topicsFromDb[0]['title'] == topic.title:
            raise HTTPException(status_code=409, detail="Thema ist bereits vorhanden.")
        else:
            with session.start_transaction:
                topic_collection.insert_one(jsonable_encoder(topic))
        return "Thema erfolgreich hinzugefügt!"
    
@topic.post('/addSolutionOption')
async def addSolutionToArray(topic: Topic):
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        topic_collection = client.get_topic_collection()
        topicsFromDb: List = topicsEntity(topic_collection.find({ "_id": ObjectId(topic.id)}))
        for solutions in topicsFromDb[0]['solutionOption']:
            if solutions == topic.solutionOption[0]:
                raise HTTPException(status_code=409, detail="Lösungsvorschlag ist bereits vorhanden.")
        else:
            with session.start_transaction:
                topic_collection.update_one({ "_id": ObjectId(topic.id)}, { '$push': {"solutionOption":{ "$each": topic.solutionOption} }})        
        return "Lösungsvorschlag erfolgreich zum Thema hinzugefügt!"    