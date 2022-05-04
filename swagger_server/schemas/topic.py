def topicEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "solutionOption": item["solutionOption"]
    }

def topicsEntity(entity) -> list:
    return [topicEntity(item) for item in entity]