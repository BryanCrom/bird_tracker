import os

from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta

load_dotenv()

class Database:
    def __init__(self, identifier) -> None:

        self.cluster = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.cluster["bird-calls"]
        self.collection = self.db["calls"]

        self.identifier = identifier

    def insert_call(self, bird_call) -> None:
        calls = self.identifier.identify(bird_call)
        for call in calls:
            call["time"] = datetime.now() - timedelta(days=4)
            call["location"] = "The Auckland Botanical Gardens"
            self.collection.insert_one(call)

    def close(self) -> None:
        self.cluster.close()