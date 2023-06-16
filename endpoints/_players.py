import json
from nba_api.stats.static import players

# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["players"]

#EXTRACT PLAYERS FULL LIST TO JSON FILE
players_dict = players.get_players()
file = 'players.json'

#SAVE INTO PLAYER.JSON FILE
with open(file, 'w') as outfile:
    json.dump(players_dict, outfile)

#SAVE INTO PLAYER COLLECTION
with open(file, 'r') as outfile:
    file_contents = json.load(outfile)
collection_name.insert_many(file_contents)
