def argumentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "topicId": item["topicId"],
        "argumentOption": item["argumentOptionEnum"],
        "solutionOption": item["solutionOption"],
        "description": item["description"],
        "date": item["date"],
        "author": item["author"],
        "approval": item["approval"],
        "links": item["links"],
        "linkedArguments": item["linkedArguments"]
    }

def argumentsEntity(entity) -> list: 
    return [argumentEntity(item) for item in entity]