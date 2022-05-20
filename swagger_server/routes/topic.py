from distutils.log import error
import logging
from bson import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from models.topic import Topic
from config.db import conn
from schemas.topic import topicEntity, topicsEntity

topic = APIRouter() 

@topic.get('/getTopics')
async def findAllTopics():
    return topicsEntity(conn.local.topic.find())

@topic.get('/findById')
async def findTopicById(searchedId: str):
    return topicsEntity(conn.local.topic.find({ "_id": ObjectId(searchedId)}))

@topic.post('/addTopic')
async def createTopic(topic: Topic):
    json_compatible_topic = jsonable_encoder(topic)
    conn.local.topic.insert_one(json_compatible_topic)
    return "Thema erfolgreich hinzugefügt!"

@topic.post('/addSolutionOption')
async def addSolutionToArray(topic: Topic):
    print(topic)
    
    try: 
        conn.local.topic.update_one(
        { "_id": ObjectId(topic.id)}, { '$push': {"solutionOption":{ "$each": topic.solutionOption} }}
        )
    except Exception as e:
        print(e.__context__)
    return "Lösungsvorschlag erfolgreich zum Thema hinzugefügt!"