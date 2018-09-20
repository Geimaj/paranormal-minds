from src.framework.request_handler import BaseRequestHandler, decorator
from apiclient.discovery import build
from oauth2client import client
from google.appengine.api import users


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
        user = users.get_current_user()

        courseName =  self.request.POST.get('courseName')
        courseHeading =  self.request.POST.get('desHeading')
        courseDescription =  self.request.POST.get('description')
        ownerID = user.user_id()
        courseState = 'PROVISIONED'

        course = {
            'name': courseName,
            'descriptionHeading': courseHeading,
            'description': courseDescription,
            'ownerId': ownerID,
            'courseState': courseState
        }

        course = service.courses().create(body=course).execute(http=decorator.http())


    
