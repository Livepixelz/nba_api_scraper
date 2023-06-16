import json
import time
import constant
import db_connect

from nba_api.stats.static import players
from nba_api.stats.endpoints import playerawards

ids = constant.PLAYERS_IDS
awardsWrapper = []
file = 'player_awards.json'
players_dict = players.get_players()

time.sleep(3)
awardsWrapper = []
active_player_iteration = 0
for (index, player) in enumerate(players_dict):
    # if active_player_iteration == 1:
    #       break
    if player['is_active'] == False:
        continue
    data = playerawards.PlayerAwards(player['id'])
    awardsData = json.loads(data.get_normalized_json())
    awards = {"id": player['id']}
    awards.update(awardsData)

    awardsWrapper.append(awards)
    print(player['full_name'] + ' awards scraped 🏀 🤖 ✏️ 📄')
    active_player_iteration += 1
    time.sleep(3)

with open(file, 'w') as outfile:
    json.dump(awardsWrapper, outfile)

with open(file, 'r') as outfile:
    file_contents = json.load(outfile)
