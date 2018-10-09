from src.framework.request_handler import BaseRequestHandler#, decorator, service
from oauth2client import client

from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)

from src.framework.api import service, decorator


class CourseHandler(BaseRequestHandler):

    @decorator.oauth_required
    def get(self, id):
        try:
            #call classorrm api and get details about course
            course = service.courses().get(id=id).execute(http=decorator.http())

            content = service.courses().courseWork().list(courseId=id).execute(http=decorator.http())

            template_parms = {
                'course': course,
                'content': content
            }

            self.render('course/course.html', **template_parms)

        except client.AccessTokenRefreshError:
            self.redirect('/')



class CreateCourse(BaseRequestHandler):
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
            #TODO redirect to new course?
            self.redirect('/course/' + course.id)

        except DeadlineExceededError  as e:
            print 'EXPECTION' * 20
            print e


class JoinCourse(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('course/joinCourse.html', **template_parms)

    def post(self):
        template_parms = {
        }

        self.response.out.write('join...')

