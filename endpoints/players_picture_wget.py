import requests  # to get image from the web
import shutil  # to save it locally
import json
import time
import os
import database

players = database.dbname['player_infos'].find()

rootPath = '/Users/okend/Sites/Lab/nba_livepixelz/players_pictures/'


def createFolder(teamId):
    folderPath = rootPath + teamId
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
    folderPath = folderPath + '/small/'
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)


def createFiles(path, filename):
    f = open(path + str(i) + filename, 'w')
    f.close()


for (index, player) in enumerate(players):
    # if player['is_active'] == False:
    #    continue
    print('🏀 ' + player['DISPLAY_FIRST_LAST'] + ' infos scraped ✅')

    actualTeamId = player['TEAM_ID']
    createFolder(str(actualTeamId))
    time.sleep(3)

    # image_url = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/' + \
    #    str(actualTeamId) + '/2020/1040x760/' + str(player['id']) + '.png'

    # image_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/' + \
    #    str(player['id']) + '.png'

    image_url = 'https://cdn.nba.com/headshots/nba/latest/260x190/' + \
        str(player['PERSON_ID']) + '.png'

    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream=True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(rootPath + str(actualTeamId) + '/small/' + filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')
