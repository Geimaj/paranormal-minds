from src.framework.api import decorator

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



# @decorator.oauth_required
def getCourses():
    # has user authenticated api access
    if decorator.has_credentials():
        # Call the Classroom API
        try:
            results = service.courses().list(pageSize=10).execute(http=decorator.http())
            enrolled_courses = results.get('courses', [])
            return enrolled_courses
        except client.AccessTokenRefreshError as e:
            print 'CLIENT ACCESS TOKEN REFRESH ERROR'
            print e
    else:
        #TODO: add link to page explaining why they should enable
        print 'no cred'
    return None