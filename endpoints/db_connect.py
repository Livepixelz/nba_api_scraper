import firebase_admin
from firebase_admin import credentials
import os.path

configPath = '/Users/okend/Sites/Lab/nba_livepixelz/config/nba-livepixelz-firebase-adminsdk-fs2hg-4ce1741283.json'

# CONNECTION TO FIREBASE
databaseURL = 'https://nba-livepixelz-default-rtdb.firebaseio.com/'
cred = credentials.Certificate(configPath)
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': databaseURL
})
