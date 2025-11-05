from src.bird_identifier.identifier import Identifier
from src.database.database import Database

database = Database(Identifier())
database.insert_call("assets/fantail.mp3")