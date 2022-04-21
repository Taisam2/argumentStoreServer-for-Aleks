def argumentEntity(item) -> dict:
    return {
        "id": str(item(["_id"])),
        "date": item("date"),
        "text": item("text"),
        "author": item("author"),
        "approval": item("approval"),
        "links": item("links"),
        "linkedArguments": item("linkedArguments")
    }

def argumentsEntity(entity) -> list: 
    return [argumentEntity(item) for item in entity]