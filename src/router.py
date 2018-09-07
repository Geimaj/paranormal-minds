import os

from oauth2client.contrib.appengine import OAuth2DecoratorFromClientSecrets
from webapp2 import WSGIApplication
from webapp2 import Route

CLIENT_SECRETS = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
    "webclient.json")

print '-' * 20
print CLIENT_SECRETS
print '-' * 20

decorator = OAuth2DecoratorFromClientSecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/classroom.courses.readonly',
    message='missing client secrets')

app = WSGIApplication(
    routes=[
        Route('/', handler='src.app.home.Home'),
        Route('/announcements', handler='src.app.announcements.Announcements'),
        Route('/course/create', handler='src.app.createCourse.CreateCourse'),
        Route(decorator.callback_path, decorator.callback_handler()),
    ]
)

