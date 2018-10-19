import logging
import os
import cloudstorage as gcs
import webapp2

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
            file = self.request.POST.get('file')

            # print
            # print '--------'
            # print
            # print file['file']
            # print '--------'
            # print
            # print

            file_metadata = {
                "name": 'Capture.jpg'
            }

            # upload file to google drive
            fileUpload = driveService.files().create(body=file_metadata,
                                        media_body=file,
                                        fields="id").execute(http=decorator.http())

            print fileUpload

            course_work = {
                'title': assTitle,
                'description': assDescription,
                'workType': 'ASSIGNMENT',
                'state': "PUBLISHED",
            }

<<<<<<< Updated upstream


            bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Demo GCS Application running from Version: '
                                + os.environ['CURRENT_VERSION_ID'] + '\n')
            self.response.write('Using bucket name: ' + bucket_name + '\n\n')            



            # course_work = service.courses().courseWork().create(courseId=id, body=course_work).execute(http=decorator.http())

            # self.response.out.write(course_work)
=======
            course_work = service.courses().courseWork().create(courseId=id, body=course_work).execute(
                http=decorator.http())

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
>>>>>>> Stashed changes

        self.render('content/submission.html', **template_parms)
