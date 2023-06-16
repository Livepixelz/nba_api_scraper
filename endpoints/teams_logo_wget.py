import requests  # to get image from the web
import shutil  # to save it locally
import json
import time
import os


from nba_api.stats.static import teams

teams_dict = teams.get_teams()

time.sleep(3)

profileInfoWrapper = []

rootPath = '/Users/okend/Sites/projects/nba-livepixelz/client/static/icons/logos/teams/'


def createFolder(teamId):
    folderPath = rootPath + teamId
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)


def createFiles(path, filename):
    f = open(path + str(i) + filename, 'w')
    f.close()


for (index, team) in enumerate(teams_dict):
    teamId = team['id']
    teamAbbr = team['abbreviation'].lower()
    time.sleep(3)
    logo_url = 'https://cdn.nba.com/logos/nba/' + \
        str(teamId)+'/global/D/logo.svg'
    filename = teamAbbr + '.svg'
    r = requests.get(logo_url, stream=True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(rootPath + filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('🏀 ' + team['full_name'] + ' logo scraped ✅', filename)
    else:
        print('Logo Couldn\'t be retreived')
