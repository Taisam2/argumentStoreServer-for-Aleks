from http.client import HTTPException
from fastapi import APIRouter
import pandas
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


@rating.get('export-csv')
async def exposrtCsv():    
    database_client = client.create_database_client()
    with database_client.start_session() as session:
        rating_collection = client.get_rating_collection()
        if not rating_collection:
            raise HTTPException(status_code=204, detail="Keine Ratings vorhanden.")
        else:
            return rating_collection.to_csv("ratings-export.csv", ",")