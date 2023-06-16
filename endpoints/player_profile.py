from nba_api.stats.endpoints import playerprofilev2
import json
import time
import database

# Find Players list
collection_name = database.dbname["players"]
players = collection_name.find()

time.sleep(3)
profileWrapper = []
for player in players:
    if player['is_active'] == False:
        continue
    data = playerprofilev2.PlayerProfileV2(player['id'])
    profileData = json.loads(data.get_normalized_json())
    profile = {"id": player['id']}
    profile.update(profileData)

    profileWrapper.append(profile)
    print('🗄️🏀 ' + player['full_name'] + ' stats scraped')

    time.sleep(1)


# SAVE INTO PLAYER COLLECTION
collection_name = database.dbname["player_profile"]
collection_name.insert_many(profileWrapper)
