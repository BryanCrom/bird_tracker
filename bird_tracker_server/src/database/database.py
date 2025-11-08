from src.database.counter import AllCounter, FantailCounter, TuiCounter, KiwiCounter, KakaCounter

import os
import random

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
        self.counter = None

    def clear_db(self):
        self.collection.delete_many({})

    def insert_call(self, bird_call) -> None:
        calls = self.identifier.identify(bird_call)

        today = datetime.today()
        days_since_sunday = (today.weekday() + 1) % 7
        last_sunday = today - timedelta(days=days_since_sunday)

        for call in calls:
            random_offset = random.randint(0, 6)
            call["time"] = last_sunday + timedelta(days=random_offset)
            call["location"] = "The Auckland Botanical Gardens"
            self.collection.insert_one(call)

    def get_calls(self, start_date, end_date, location, bird_name) -> list:

        results = []

        start_date = datetime.fromtimestamp(start_date / 1000)
        end_date = datetime.fromtimestamp(end_date / 1000)

        current_day = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_day = end_date.replace(hour=0, minute=0, second=0, microsecond=0)

        match bird_name:
            case "all":
                self.counter = AllCounter(self)
            case "fantail":
                self.counter = FantailCounter(self)
            case "tui":
                self.counter = TuiCounter(self)
            case "kiwi":
                self.counter = KiwiCounter(self)
            case "kaka":
                self.counter = KakaCounter(self)

        while current_day <= end_day:
            next_day = current_day + timedelta(days=1)

            count = self.counter.get_count(current_day, next_day, location)
            results.append({"count": count, "day": (current_day.weekday() + 1) % 7})


            current_day = next_day
        return results

    def populate_db(self):
        folder_path = "assets"

        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    self.insert_call("assets/" + entry.name)

    def clear_database(self):
        self.collection.delete_many({})


    def close(self) -> None:
        self.cluster.close()