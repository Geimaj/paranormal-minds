from webapp2 import RequestHandler
import os
import jinja2

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

# from src.models import course



class BaseRequestHandler(RequestHandler):
    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        "templates")

    jinja_enviroment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir)
    )

    
    def render(self, template, **kwargs):
        jinja_template = self.jinja_enviroment.get_template(template)

        nickname = ''
        logout_url = ''
        login_url = ''
        enrolled_courses = []

        user = users.get_current_user()
        if (user):
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            enrolled_courses = self.getCourses()

        else:
            login_url = users.create_login_url('/')


        kwargs['username'] = nickname
        kwargs['logout_url'] = logout_url
        kwargs['login_url'] = login_url
        kwargs['enrolled_courses'] = enrolled_courses

        template_html = jinja_template.render(kwargs)

        self.response.out.write(template_html)



    #TODO: MOVE THIS
    @decorator.oauth_required
    def getCourses(self):
        #has user authenticated api access
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
            print 'no cred'
        return None