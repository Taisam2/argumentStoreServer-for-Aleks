from pymongo import MongoClient
from argument_store.config.util import DbUtil


u = DbUtil()

#or not conn.get_database("ArgumentStore").get_collection("local.argument")
conn_string = "mongodb+srv://" + u.username +":" + u.passwort + "@argumentstore.lkyrg.mongodb.net/?retryWrites=true&w=majority"

conn = MongoClient(conn_string, serverSelectionTimeoutMS=5000)

try:
    print("Server is running with the following properties:\n")
    print(conn.server_info)
    #raise HTTPException(status_code=504, detail="Verbindung zur Datenbank unterbrochen.")
except Exception as e:
    print("DB-connection failed: \n")
    print(e)


