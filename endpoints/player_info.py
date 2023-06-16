from nba_api.stats.endpoints import commonplayerinfo
import json
import time
import database

# Find Players list
collection_name = database.dbname["players"]
players = collection_name.find()


time.sleep(3)

profileInfoWrapper = []
print()

for player in players:
    if player['is_active'] == False:
        continue
    data = commonplayerinfo.CommonPlayerInfo(player['id'])
    profileInfo = json.loads(data.get_normalized_json())
    profileInfoWrapper.extend(profileInfo['CommonPlayerInfo'])
    print('🏀 ' + player['full_name'] + ' infos scraped ✅')
    time.sleep(1)

# SAVE INTO PLAYER COLLECTION
print(profileInfoWrapper)
# Create a new collection
collection_name = database.dbname["player_infos"]
collection_name.insert_many(profileInfoWrapper)
