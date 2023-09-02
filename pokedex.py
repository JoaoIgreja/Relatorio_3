import json
from database import Database

class Pokedex:
    def __init__(self):
        self.db = Database()

pokemon = db.collection.find_one({"name": "Bulbasaur"})
writeAJson(pokemon, "pokemon")