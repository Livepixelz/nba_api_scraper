import json
import time
import constant
import db_connect
from firebase_admin import db

from nba_api.stats.endpoints import playercareerstats

ref = db.reference("/PlayerCareerStats")

ids = constant.PLAYERS_IDS
statsWrapper = []
file = 'player_career_stats.json'
for id in ids:
    data = playercareerstats.PlayerCareerStats(player_id=id)
    stats = json.loads(data.get_normalized_json())
    print(stats)
    statsWrapper.extend(stats['SeasonTotalsRegularSeason'])
    time.sleep(1)

with open(file, 'w') as outfile:
    json.dump(statsWrapper, outfile)

with open(file, 'r') as outfile:
    file_contents = json.load(outfile)
ref.set(file_contents)
