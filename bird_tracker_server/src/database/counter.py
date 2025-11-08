class Counter:
    def __init__(self, database):
        self.database = database

class AllCounter(Counter):
    def get_count(self, current_day, next_day, location):
        return self.database.collection.count_documents({"time": {"$gte": current_day, "$lte": next_day}, "location": location})

class FantailCounter(Counter):
    def get_count(self, current_day, next_day, location):
        return self.database.collection.count_documents({"time": {"$gte": current_day, "$lte": next_day}, "location": location, "common_name": "New Zealand Fantail"})

class TuiCounter(Counter):
    def get_count(self, current_day, next_day, location):
        return self.database.collection.count_documents({"time": {"$gte": current_day, "$lte": next_day}, "location": location, "common_name": "Tui"})

class KiwiCounter(Counter):
    def get_count(self, current_day, next_day, location):
        return self.database.collection.count_documents({"time": {"$gte": current_day, "$lte": next_day}, "location": location, "common_name": "North Island Brown Kiwi"})

class KakaCounter(Counter):
    def get_count(self, current_day, next_day, location):
        return self.database.collection.count_documents({"time": {"$gte": current_day, "$lte": next_day}, "location": location, "common_name": "New Zealand Kaka"})