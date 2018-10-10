from src.framework.request_handler import BaseRequestHandler
from oauth2client import client

from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)

from src.framework.api import service, decorator

import src.models as models


class CourseHandler(BaseRequestHandler):

    @decorator.oauth_required
    def get(self, id):
        try:
            #call classroom api and get details about course
            course = service.courses().get(id=id).execute(http=decorator.http())

            #fetch teachers for this course
            teachers = []
            teacher_results = service.courses().teachers().list(courseId=id).execute(http=decorator.http())
            if teacher_results['teachers']:
                teachers = teacher_results['teachers']
            
            # fetch students for this course
            students = []
            student_results = service.courses().students().list(courseId=id).execute(http=decorator.http())
            if student_results['students']:
                students = student_results['students']

            #fetch content for this course
            content = service.courses().courseWork().list(courseId=id).execute(http=decorator.http())

            # fetch announcements for this course
            announcements = models.Announcement.get_by_courseID(id)
            
            userProfile = service.userProfiles().get(userId='me').execute(http=decorator.http())
            userId = userProfile['id']

            isTeacher = models.Course.isUserTeacher(id, userId)
            print isTeacher

            template_parms = {
                'title': course['name'],
                'isTeacher': isTeacher,
                'course': course,
                'content': content,
                'courseId' : id,
                'announcements': announcements,
                'teachers': teachers,
                'students': students
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


class CourseDetailsHandler(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseID):

        # fetch course by id
        course = models.Course.get_by_id(courseID)

        template_parms = {
            'course': course
        }

        self.render('course/details.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseID):
        try:
                
            # get reference to course object 
            course = models.Course.get_by_id(courseID)

            # get updated values from form
            post = self.request.POST
            name = post.get('name')
            section = post.get('section')
            descriptionHeading = post.get('description-heading')
            description = post.get('description')
            room = post.get('room')
            courseState = post.get('courseState')

            #assign new values from form to course 
            course['name'] = name
            course['section'] = section
            course['descriptionHeading'] = descriptionHeading
            course['description'] = description
            course['room'] = room
            course['courseState'] = courseState

            # call api to update course
            service.courses().update(id=courseID, body=course).execute(http=decorator.http())

            # display updated course details page
            self.redirect('/course/%s' % courseID)
        except Exception as e:
            print e


