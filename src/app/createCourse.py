from src.framework.request_handler import BaseRequestHandler
from apiclient.discovery import build
from oauth2client.contrib.appengine import OAuth2Decorator
from oauth2client.contrib.appengine import OAuth2DecoratorFromClientSecrets
from oauth2client import client

# decorator = OAuth2Decorator(
#   client_id='355461818608-lsc3c0adqfkn9gddcba24fmoajhma8h7.apps.googleusercontent.com',
#   client_secret='FnH17qv2k-eeSxZ9XZSJiPN9',
#   scope='https://www.googleapis.com/auth/classroom.courses.readonly'
# )

# decorator = OAuth2DecoratorFromClientSecrets(
#     'client_secrets.json',
#     scope='https://www.googleapis.com/auth/classroom.courses.readonly',
#     message='missing client secrets')
from src.router import decorator

service = build('classroom', 'v1')


class CreateCourse(BaseRequestHandler):


    @decorator.oauth_required
    def get(self):
        try:
            # Call the Classroom API
            results = service.courses().list(pageSize=10).execute()
            courses = results.get('courses', [])

            if not courses:
                print('No courses found.')
            else:
                print('Courses:')
                for course in courses:
                    print(course['name'])

            template_parms = {
            }

            self.render('course/createCourse.html', **template_parms)

        except client.AccessTokenRefreshError:
            self.redirect('/')



    @decorator.oauth_required
    def post(self):
        courseName =  self.request.POST.get('courseName')
        courseHeading =  self.request.POST.get('desHeading')
        courseDescription =  self.request.POST.get('description')
        ownerID = 0
        courseState = 'PROVISIONED'

        course = {
            'name': courseName,
            'descriptionHeading': courseHeading,
            'description': courseDescription,
            'ownerId': ownerID,
            'courseState': courseState
        }


        course = service.courses().create(body=course).execute()


    
