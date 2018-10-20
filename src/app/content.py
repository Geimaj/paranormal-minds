import logging
import os

from google.appengine.api import app_identity

from src.framework.request_handler import BaseRequestHandler
from src.framework.api import service, decorator, client, driveService

# import our models
import src.models as models

#import google users api
from google.appengine.api import users

class ContentHandler(BaseRequestHandler):
    def get(self, courseId):

        course = models.Course.get_by_id(courseId)

        template_parms = {
                'courseId' : courseId,
                'course' : course
         }

        self.render('content/content.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseId):
        try:
            id = self.request.POST.get('courseId')
            assTitle = self.request.POST.get('assTitle')
            assDescription = self.request.POST.get('assDescription')

            course_work = {
                'title': assTitle,
                'description': assDescription,
                'workType': 'ASSIGNMENT',
                'state': "PUBLISHED",
            }

            course_work = service.courses().courseWork().create(courseId=id, body=course_work).execute(http=decorator.http())

            self.response.out.write(course_work)

            # get data from form
            # based on the name of the input element in the form
            # id = self.request.POST.get('courseId')
            # title = self.request.POST.get('asstitle')
            # description = self.request.POST.get('assDescription')
            #
            #

            # get current user
            user = users.get_current_user()
            # get id of user
            ownerId = user.user_id()
            email = user.email()

            # create announcement object from our models
            announcement = models.Announcement()

            # pass data to announcemnt object
            announcement.title = assTitle
            announcement.content = assDescription
            announcement.courseId = id
            announcement.ownerId = ownerId
            announcement.ownerEmail = email

            # write to db
            announcement.put()
            self.response.out.write(announcement)

            self.redirect('/course/%s' % courseId)


        except Exception as e:
            self.response.out.write(e)

class SubmissionHandler(BaseRequestHandler):

    # @decorator.oauth_required
    def get(self):

        print "HERE" *20

        template_parms = {

        }
        self.render('content/submission.html', **template_parms)
