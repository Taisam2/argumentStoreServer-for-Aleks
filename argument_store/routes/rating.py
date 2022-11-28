from typing import List
from fastapi import APIRouter
import pandas as pd
import os 
from argument_store.config.db import DatabaseClient
from argument_store.models.rating.rating import Rating

from argument_store.schemas.rating import ratingsEntity

from fastapi.encoders import jsonable_encoder

rating = APIRouter()

client = DatabaseClient()

@rating.get('/rating-solution/{solution}')
async def findRatingWithSolution():
    return None


@rating.post('/addRating')
async def addRating(rating: Rating):
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        rating_collection = client.get_rating_collection()
        with session.start_transaction():
            rating_collection.insert_one(jsonable_encoder(rating))  
            session.commit_transaction()     
            session.end_session()
    return "Rating erfolgreich hinzugefügt!"

@rating.post('/addRatings')
async def addRatings(ratings: list[Rating]):
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        rating_collection = client.get_rating_collection()
        with session.start_transaction():
            for rating in ratings:
                rating_collection.insert_one(jsonable_encoder(rating))  
            session.commit_transaction()     
            session.end_session()
    return "Rating erfolgreich hinzugefügt!"

@rating.get('/allRatings')
async def exposrtCsv():    
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        rating_collection = client.get_rating_collection()
        response: List = ratingsEntity(rating_collection.find(session=session))
        return response


@rating.get('/export-csv')
async def exposrtCsv():    
    database_client = client.create_database_client()
    pc_username = os.getlogin()
    download_path = "C:/Users/"+ pc_username +"/Downloads/ratings-export.csv"
    with database_client.start_session() as session:
        rating_collection = client.get_rating_collection()
        response: List = ratingsEntity(rating_collection.find(session=session))
        return pd.DataFrame({'ratings:': response}).to_csv(download_path)