from pymongo import MongoClient
from argument_store.config.util import DbUtil


u = DbUtil()

try:
    conn = MongoClient("mongodb+srv://" + u.username +":" + u.passwort + "@argumentstore.lkyrg.mongodb.net/?retryWrites=true&w=majority")
except Exception as e:
    print("Db-connection Error: " + e)



