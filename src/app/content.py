import logging
import os

from google.appengine.api import app_identity
from apiclient.http import MediaFileUpload

from src.framework.request_handler import BaseRequestHandler, jinja2
from src.framework.api import service, decorator, client, driveService

# import our models
import src.models as models

#import google users api
from google.appengine.api import users

class ContentHandler(BaseRequestHandler):
    def get(self, courseId):
        upload_url ='/content/createAssignment'

        template_parms = {
            'courseId' : courseId,
            'uploadUrl': upload_url
        }

        self.render('content/content.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseId):
        try:
            id = self.request.POST.get('courseId')
            id = jinja2.escape(id)
            assTitle = self.request.POST.get('assTitle')
            assTitle = jinja2.escape(assTitle)
            assDescription = self.request.POST.get('assDescription')
            assDescription = jinja2.escape(assDescription)
            fileUrl = self.request.POST.get('fileUrl')
            fileUrl = jinja2.escape(fileUrl);

            course_work = {
                'title': assTitle,
                'description': assDescription,
                'workType': 'ASSIGNMENT',
                'state': "PUBLISHED",
                'materials': { 'link': { 'url': fileUrl }}
            }

            course_work = service.courses().courseWork().create(courseId=id, body=course_work).execute(http=decorator.http())

            self.response.out.write(course_work)

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

