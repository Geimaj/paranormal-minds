from src.framework.request_handler import BaseRequestHandler, decorator, service
# from apiclient.discovery import build
from oauth2client import client



# service = build('classroom', 'v1')


class CourseHandler(BaseRequestHandler):

    @decorator.oauth_required
    def get(self, id):
        try:

            #call classorrm api and get details about course
            course = service.courses().get(id=id).execute(http=decorator.http())

            print course

            template_parms = {
                'course': course
            }

            self.render('course/course.html', **template_parms)

        except client.AccessTokenRefreshError:
            self.redirect('/')
