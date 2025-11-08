from src.bird_identifier.identifier import Identifier
from src.database.database import Database
from src.api.api import API

identifier = Identifier()
database = Database(identifier)

choice = input("do you wish to populate the database for the current week? y/n: ")
if choice == "y":
    database.populate_db()
elif choice == "clear":
    database.clear_database()

api = API(database)
api.run()