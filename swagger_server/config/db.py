from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")


client = MongoClient('mongodb://localhost:27017/')
result = client['local']['argument'].aggregate([
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
])