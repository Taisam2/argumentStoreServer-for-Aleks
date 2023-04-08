from pymongo import MongoClient
import pymongo
from argument_store.config.util import DbUtil
import logging

class DatabaseClient():

    def __init__(self):
        self._db_util = DbUtil()
        self._conn_string = "mongodb+srv://" + self._db_util.username +":" + self._db_util.passwort + "@<ADD YOUR MONGODB DOMAIN NAME>"

    def create_database_client(self):
        try:
            self._client = MongoClient(self._conn_string, serverSelectionTimeoutMS=5000)
            try:
                self._client.server_info()
                return self._client
            except Exception as e:
                logging.error("Connection failed!! Error Message: %s %s" % (type(e),e))
        except pymongo.errors.ConnectionFailure as e:
            logging.error("Client couldn't be created! Error Message: %s %s" % (type(e),e))

    def get_argument_collection(self):
        return self._client.ArgumentStore.local.argument

    def get_topic_collection(self):
        return self._client.ArgumentStore.local.topic

    def get_rating_collection(self):
        return self._client.ArgumentStore.local.rating
