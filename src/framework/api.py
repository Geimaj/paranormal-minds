import os

import httplib2

from oauth2client.contrib.appengine import OAuth2DecoratorFromClientSecrets
from google.appengine.api import users, memcache
from apiclient.discovery import build
from oauth2client import client

http= httplib2.Http(cache=memcache)

service = build('classroom', 'v1', http)
driveService = build('drive', 'v3', http)

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

CLIENT_SECRETS = os.path.abspath(os.path.join(parent_dir, 'credentials.json'))

SCOPES = [
    'https://www.googleapis.com/auth/classroom.coursework.me',
    'https://www.googleapis.com/auth/classroom.courses',
    'https://www.googleapis.com/auth/classroom.coursework.students',
    'https://www.googleapis.com/auth/classroom.rosters',
    'https://www.googleapis.com/auth/drive'
]

decorator = OAuth2DecoratorFromClientSecrets(
    CLIENT_SECRETS,
    scope=SCOPES)
