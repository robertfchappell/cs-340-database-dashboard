from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username="aacuser", password="SNHU1234"):
        # Connection Variables
        USER = username
        PASS = password
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        # Initialize Connection
        # aacuser authenticates against the admin database
        uri = "mongodb://%s:%s@%s:%d/?authSource=admin" % (USER, PASS, HOST, PORT)

        self.client = MongoClient(uri)
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Complete this create method to implement the C in CRUD.
    # Return True if successful insert, else False
    def create(self, data):
        if data is None:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged is True
        except PyMongoError:
            return False
        except Exception:
            return False

    # Create method to implement the R in CRUD.
    # Use find() (not find_one()) and return a list, else empty list
    def read(self, query):
        if query is None:
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError:
            return []
        except Exception:
            return []

    # Update method to implement the U in CRUD.
    # Input: query dict + update_data dict
    # Return: number of objects modified in the collection
    def update(self, query, update_data):
        if query is None or update_data is None:
            return 0

        try:
            # If update_data is plain fields, wrap it in $set
            if not any(k.startswith("$") for k in update_data.keys()):
                update_data = {"$set": update_data}

            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except PyMongoError:
            return 0
        except Exception:
            return 0

    # Delete method to implement the D in CRUD.
    # Input: query dict
    # Return: number of objects removed from the collection
    def delete(self, query):
        if query is None:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError:
            return 0
        except Exception:
            return 0
