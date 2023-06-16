import json
import db_connect
from nba_api.stats.static import teams
from firebase_admin import db

ref = db.reference("/Teams")
# EXTRACT PLAYERS FULL LIST TO JSON FILE
teams_dict = teams.get_teams()
file = './data/teams.json'

with open(file, 'w') as outfile:
    json.dump(teams_dict, outfile)

# IMPORT JSON PLAYERS FULL LIST TO FIREBASE DB
with open(file, 'r') as outfile:
    file_contents = json.load(outfile)

ref.set(file_contents)
