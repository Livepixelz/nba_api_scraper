import json
import time
import db_connect
from firebase_admin import db

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
ref = db.reference("/PlayerInfo")

# Basic Request
# Get all players list
players_dict = players.get_players()

time.sleep(3)

profileInfoWrapper = []
file = 'player_infos.json'

for (index, player) in enumerate(players_dict):
    if player['is_active'] == False:
        continue
    # if player['id'] == 2544:
    data = commonplayerinfo.CommonPlayerInfo(player['id'])
    profileInfo = json.loads(data.get_normalized_json())
    profileInfoWrapper.extend(profileInfo['CommonPlayerInfo'])
    print('🏀 ' + player['full_name'] + ' infos scraped ✅')
    time.sleep(3)

with open(file, 'w') as outfile:
    json.dump(profileInfoWrapper, outfile)

with open(file, 'r') as outfile:
    file_contents = json.load(outfile)
