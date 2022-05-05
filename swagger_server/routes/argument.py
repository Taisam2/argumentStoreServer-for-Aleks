from fastapi import APIRouter
from config.db import conn, result
from models.argument import Argument
from schemas.argument import argumentsEntity

from fastapi.encoders import jsonable_encoder

argument = APIRouter()

pipeline = [
    {
        '$lookup': {
            'from': 'argument', 
            'let': {
                'solOpt': '$solutionOption', 
                'argsOpt': '$argumentOption'
            }, 
            'pipeline': [
                {
                    '$match': {
                        '$expr': {
                            '$and': [
                                {
                                    '$eq': [
                                        '$argumentOption', '$$argsOpt'
                                    ]
                                }
                            ]
                        }
                    }
                }
            ], 
            'as': 'comments'
        }
    }, {
        '$group': {
            '_id': '$comments'
        }
    }
]

@argument.get('/getArguments')
async def findAllArguments():
    return argumentsEntity(conn.local.argument.find())

@argument.get('/getArgumentsByArgOpt')
async def getSortedAgruments():
    resultsArr = []
    results = argumentsEntity(conn.local.argument.aggregate(pipeline))
    for e in results:
        print("Array position")
        print(e)
        resultsArr.append(e)
    json_compatible_argument_array = jsonable_encoder(resultsArr)    
    return json_compatible_argument_array

@argument.post('/addArgument')
async def createArgument(argument: Argument):
    json_compatible_argument = jsonable_encoder(argument)
    conn.local.argument.insert_one(json_compatible_argument)
    return "Successful added a Argument!"


