from nba_api.stats.endpoints import commonteamroster
import json
import time

import database

# Find Teams list
teams = database.dbname["teams"].find()


time.sleep(3)
rostersWrapper = []

for (index, team) in enumerate(teams):
    data = commonteamroster.CommonTeamRoster(team['id'])
    rosterData = json.loads(data.get_normalized_json())
    roster = {"id": team['id']}
    roster.update(rosterData)

    rostersWrapper.append(roster)
    print('📄 🔽 🤖' + team['full_name'] + ' roster scraped')
    time.sleep(1)


# SAVE INTO TEAM ROSTER COLLECTION
collection_name = database.dbname["team_roster"]
collection_name.insert_many(rostersWrapper)
