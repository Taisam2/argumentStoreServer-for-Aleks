from pymongo import MongoClient
from config.util import DbUtil
from urllib.parse import quote_plus

u = DbUtil()

try:
    conn = MongoClient("mongodb+srv://" + u.username +":" + u.passwort + "@argumentstore.lkyrg.mongodb.net/?retryWrites=true&w=majority")
except Exception as e:
    print("Db-connection Error: " + e)



