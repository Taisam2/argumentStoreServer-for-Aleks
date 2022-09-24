def ratingEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "optionNumber": item["optionNumber"],
        "optionName": item["optionName"],
        "sol_rat_1": item["sol_rat_1"],
        "sol_rat_2": item["sol_rat_2"],
        "sol_rat_3": item["sol_rat_3"],
        "date": item["date"]
    }

def argumentsEntity(entity) -> list: 
    return [ratingEntity(item) for item in entity]