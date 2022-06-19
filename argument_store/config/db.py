from fastapi import HTTPException
from pymongo import MongoClient
from argument_store.config.util import DbUtil


u = DbUtil()

#or not conn.get_database("ArgumentStore").get_collection("local.argument")

conn = MongoClient("mongodb+srv://" + u.username +":" + u.passwort + "@argumentstore.lkyrg.mongodb.net/?retryWrites=true&w=majority")

if not conn:
    raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
else:
    print("Server is running with the following properties:\n")
    print(conn.server_info)


