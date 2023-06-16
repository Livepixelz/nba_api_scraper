import json
import time
import db_connect
from firebase_admin import db

from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats

# Get all teams list
teams_dict = teams.get_teams()

time.sleep(3)
detailsWrapper = []
file = 'team_yearbyyearstats.json'
for (index, team) in enumerate(teams_dict):
    data = teamyearbyyearstats.TeamYearByYearStats(team['id'])
    detailData = json.loads(data.get_normalized_json())
    detail = {"id": team['id']}
    detail.update(detailData)

    detailsWrapper.append(detail)
    print('📄 🔽 🤖' + team['full_name'] + ' year by year stats scraped')
    time.sleep(3)


with open(file, 'w') as outfile:
    json.dump(detailsWrapper, outfile)

with open(file, 'r') as outfile:
    file_contents = json.load(outfile)
