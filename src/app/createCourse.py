from src.framework.request_handler import BaseRequestHandler, decorator
from apiclient.discovery import build
from oauth2client import client
from google.appengine.api import users
from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)

service = build('classroom', 'v1')

class CreateCourse(BaseRequestHandler):
    @decorator.oauth_required
    def get(self):
        try:
           
            template_parms = {
            }

            self.render('course/createCourse.html', **template_parms)

        except client.AccessTokenRefreshError:
            self.redirect('/')


    @decorator.oauth_required
    def post(self):
        try:

            courseName =  self.request.POST.get('courseName')
            courseHeading =  self.request.POST.get('desHeading')
            courseDescription =  self.request.POST.get('description')
            ownerID = 'me'
            courseState = 'PROVISIONED'

            course = {
                'name': courseName,
                'descriptionHeading': courseHeading,
                'description': courseDescription,
                'ownerId': ownerID,
                'courseState': courseState
            }

            course = service.courses().create(body=course).execute(http=decorator.http())
            self.redirect('/')

        except DeadlineExceededError  as e:
            print 'EXPECTION' * 20
            print e

