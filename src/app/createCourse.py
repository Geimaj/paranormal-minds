from src.framework.request_handler import BaseRequestHandler, decorator
from apiclient.discovery import build
from oauth2client import client

service = build('classroom', 'v1')

class CreateCourse(BaseRequestHandler):
    @decorator.oauth_required
    def get(self):
        try:
            # Call the Classroom API
            results = service.courses().list(pageSize=10).execute(http=decorator.http())
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


    
