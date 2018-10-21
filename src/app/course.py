from oauth2client import client
import json as simplejson
import googleapiclient.errors as errors
from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(10000)

from src.framework.api import service, decorator
from src.framework.request_handler import BaseRequestHandler
import src.models as models

class CourseHandler(BaseRequestHandler):

    @decorator.oauth_required
    def get(self, id):
        try:
            #call classroom api and get details about course
            course = service.courses().get(id=id).execute(http=decorator.http())

            #fetch teachers for this course
            teacher_results = service.courses().teachers().list(courseId=id).execute(http=decorator.http())
            
            # fetch students for this course
            student_results = service.courses().students().list(courseId=id).execute(http=decorator.http())

            # fetch content for this course
            content_results = service.courses().courseWork().list(courseId=id).execute(http=decorator.http())

            #get data we are inretested in from api results
            students = []
            teachers = []
            content = []
            discussionTopic = []
            try:
                discussionTopic = models.DiscussionTopic.query().fetch()
                students = student_results['students']
                teachers = teacher_results['teachers']
                content = content_results['courseWork']
                discussionTopics = models.DiscussionTopic.query().fetch()
            except Exception as e:
                print "ERROR extracting results from api in course.py" * 20
                print e

            # fetch announcements for this course
            announcements = models.Announcement.get_by_courseID(id)

            userProfile = service.userProfiles().get(userId='me').execute(http=decorator.http())
            userId = userProfile['id']

            isTeacher = models.Course.isUserTeacher(id, userId)

            courseState = course['courseState']
            showBanner = courseState == "ACTIVE"

            print
            print
            print showBanner 
            print

            template_parms = {
                'title': course['name'],
                'isTeacher': isTeacher,
                'course': course,
                'content': content,
                'courseId' : id,
                'announcements': announcements,
                'teachers': teachers,
                'students': students,
                'discussionTopics': discussionTopic,
                'activateCourseBanner': showBanner
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

            self.redirect('/course/' + course['id'])

        except Exception as e:
            print 'ERRPR CREATING COURSE' * 6
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
            if courseState:
                course['courseState'] = courseState

            # call api to update course
            service.courses().update(id=courseID, body=course).execute(http=decorator.http())

            # display updated course details page
            self.redirect('/course/%s' % courseID)
        except errors.HttpError as e:
            error = simplejson.loads(e.content).get('error')

            message = str(error.get('message'))

            if(message.startswith('@CourseNotModifiable')):
                self.response.out.write('cant update course wiht courseState: %s ' % course['courseState'])
                # self.redirect('/course/%s' % courseID)
                
            else:
                raise



class LeaveCourseHandler(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseID):

        # fetch course by id
        course = models.Course.get_by_id(courseID)

        template_parms = {
            'course': course
        }

        self.render('course/leave.html', **template_parms)


    @decorator.oauth_required
    def post(self, courseID):

        #leave course
        try:
            userProfile = service.userProfiles().get(userId='me').execute(http=decorator.http())
            userId = userProfile['id']

            course = models.Course.get_by_id(courseID)
            print course
            print 
            print userProfile

            # do I remove myself as a student or as a teacher
            result = ''
            if models.Course.isUserTeacher(courseID, userId):
                print 'TEACHER'
                result = service.courses().teachers().delete(courseId=courseID, userId=userId).execute(http=decorator.http())
            else:
                print 'STUD'
                result = service.courses().students().delete(courseId=courseID, userId=userId).execute(http=decorator.http())
    
            print result

            self.redirect('/courses')
        except Exception as e:
            print e


class StateChangeHandler(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseID):

        # course = service.courses().get(id=courseID).execute(decorator.http())
        course = models.Course.get_by_id(courseID)
        course['courseState'] = 'ACTIVE'

        try:
            # call api to update course
            service.courses().update(id=courseID, body=course).execute(http=decorator.http())
            self.redirect('/course/%s' % courseID)
        except Exception as e:
            self.response.out.write('ERROR')
            self.response.out.write(e)


