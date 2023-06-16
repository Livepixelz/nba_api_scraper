import requests  # to get image from the web
import shutil  # to save it locally
import json
import time
import os


#from nba_api.stats.static import players
#from nba_api.stats.endpoints import commonplayerinfo

# EXTRACT PLAYERS FULL LIST TO JSON FILE
#players_dict = players.get_players()

# time.sleep(3)

# with open(file, 'w') as outfile:
#    json.dump(players_dict, outfile)
rostersWrapper = []

playersFile = 'playersmissing.json'
with open(playersFile, 'r') as outfileT:
    file_contents = json.load(outfileT)

profileInfoWrapper = []

rootPath = '/Users/okend/Sites/Lab/nba_livepixelz/players_pictures/'


def createFolder(teamId):
    folderPath = rootPath + teamId + '/large/'
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)


def createFiles(path, filename):
    f = open(path + str(i) + filename, 'w')
    f.close()


start = 0

for (index, player) in enumerate(file_contents):
    if player['is_active'] == False:
        continue

    actualTeamId = player['team_id']
    createFolder(str(actualTeamId))
    time.sleep(3)

    # image_url = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/' + \
    #    str(actualTeamId) + '/2020/1040x760/' + str(player['id']) + '.png'

    # image_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/' + \
    #    str(player['id']) + '.png'

    image_url = 'https://cdn.nba.com/headshots/nba/latest/260x190/' + \
        str(player['id']) + '.png'

    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream=True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(rootPath + str(actualTeamId) + '/' + filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('✅ Image of ' + player['full_name'] + ' downloaded: ', filename)
    else:
        print('🚫 Image of ' + player['full_name'] + ' couldn\'t be retreived')
