import json


def findIndex(flist, func):
    for i, v in enumerate(flist):
        if func(v):
            return i
    return -1


def hasId(p):
    if p["id"] == data["id"]:
        return True
    else:
        return False


# EXTRACT PLAYERS FULL LIST TO JSON FILE
teamsFile = 'team_rosters.json'
playersFile = 'players.json'
outputFile = 'playersmissing.json'
# with open(file, 'w') as outfile:
#    json.dump(players_dict, outfile)
rostersWrapper = []
# IMPORT JSON PLAYERS FULL LIST TO FIREBASE DB
with open(teamsFile, 'r') as outfileT:
    file_contents = json.load(outfileT)

with open(playersFile, 'r') as outfileP:
    players_content = json.load(outfileP)

print(players_content)

iteration = 0
for team in file_contents:
    teamRoster = team['CommonTeamRoster']

    for player in teamRoster:

        data = {"id": player["PLAYER_ID"], "full_name": player["PLAYER"], "first_name": player["NICKNAME"],
                "last_name": player["PLAYER"].replace(player["NICKNAME"], '').replace(' ', '', 1), "team_id": player["TeamID"], "is_active": True}
        #playerData = json.dumps(data)

        if findIndex(players_content, hasId) != -1:
            print(data["full_name"] + ' is already in players list')
            continue
        rostersWrapper.append(data)
        # players_content.append(data)


# with open(playersFile, 'w') as outfile:
#    json.dump(players_content, outfile)

with open(outputFile, 'w') as outfile:
    json.dump(rostersWrapper, outfile)
