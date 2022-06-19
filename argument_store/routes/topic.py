from bson import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from argument_store.models.topic.topic import Topic
from argument_store.config.db import conn
from argument_store.schemas.topic import topicsEntity

topic = APIRouter() 

@topic.get('/getTopics')
async def findAllTopics():
    try:
        rsp = topicsEntity(conn.ArgumentStore.local.topic.find())
        if rsp == []:
            return print("Bisher sind keine Themen gespeichert.")
        return topicsEntity(conn.ArgumentStore.local.topic.find())
    except Exception as e:
        print("Error in /getTopics route: ")

@topic.get('/findById')
async def findTopicById(searchedId: str):
    try:
        if not topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(searchedId)})):
            return "Thema mit der id: " + searchedId + " ist nicht vorhanden."
        return topicsEntity(conn.ArgumentStore.local.topic.find({ "_id": ObjectId(searchedId)}))
    except Exception as e:
        print("Error in /findById Topics route: ") 

@topic.post('/addTopic')
async def createTopic(topic: Topic):
    try:
        conn.ArgumentStore.local.topic.insert_one(jsonable_encoder(topic))
        return "Thema erfolgreich hinzugefügt!"
    except Exception as e:
        print("Error in /addTopic route: ") 

@topic.post('/addSolutionOption')
async def addSolutionToArray(topic: Topic):
    try: 
        conn.ArgumentStore.local.topic.update_one(
        { "_id": ObjectId(topic.id)}, { '$push': {"solutionOption":{ "$each": topic.solutionOption} }}
        )
        return "Lösungsvorschlag erfolgreich zum Thema hinzugefügt!"
    except Exception as e:
        print("Error in /addSolutionOption route: ")
    