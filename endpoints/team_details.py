from nba_api.stats.endpoints import teamdetails
import json
import time

import database

# Find Teams list
teams = database.dbname["teams"].find()


time.sleep(3)
detailsWrapper = []

for (index, team) in enumerate(teams):
    data = teamdetails.TeamDetails(team['id'])
    detailData = json.loads(data.get_normalized_json())
    detail = {"id": team['id']}
    detail.update(detailData)

    detailsWrapper.append(detail)
    print('📄 🔽 🤖' + team['full_name'] + ' detail scraped')
    time.sleep(1)


# SAVE INTO TEAM DETAILS COLLECTION
collection_name = database.dbname["team_details"]
collection_name.insert_many(detailsWrapper)
