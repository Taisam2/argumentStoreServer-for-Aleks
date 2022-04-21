from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from swagger_server.models.topic import Topic
from config.db import conn
from swagger_server.schemas.topic import topicEntity, topicsEntity
from swagger_server.schemas.argument import argumentEntity, argumentsEntity

topic = APIRouter() 

@topic.get('/')
async def findAllTopics():
    return topicsEntity(conn.local.topic.find())


@topic.post('/')
async def createTopic(topic: Topic):
    json_compatible_topic = jsonable_encoder(topic)
    conn.local.topic.insert_one(json_compatible_topic)
    return ""