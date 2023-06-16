import json
import database
from nba_api.stats.endpoints import alltimeleadersgrids

collection_name = database.dbname['alltime_leaders_grid']

data = alltimeleadersgrids.AllTimeLeadersGrids()
stats = json.loads(data.get_normalized_json())

print(stats)
# SAVE INTO PLAYER COLLECTION
collection_name.insert_one(stats)
