import os


from oauth2client.contrib.appengine import OAuth2DecoratorFromClientSecrets
from google.appengine.api import users
from apiclient.discovery import build
from oauth2client import client

service = build('classroom', 'v1')
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

CLIENT_SECRETS = os.path.abspath(os.path.join(parent_dir, 'credentials.json'))

decorator = OAuth2DecoratorFromClientSecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/classroom.courses')
