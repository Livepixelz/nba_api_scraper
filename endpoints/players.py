import json
import database
from nba_api.stats.static import players

collection_name = database.dbname["players"]
players_dict = players.get_players()

# SAVE INTO PLAYER COLLECTION
collection_name.insert_many(players_dict)
