import logging
import os
import cloudstorage as gcs
import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import app_identity
from apiclient.http import MediaFileUpload

from src.framework.request_handler import BaseRequestHandler
from src.framework.api import service, driveService, decorator, client



class ContentHandler(BaseRequestHandler):
    def get(self, courseId):
        upload_url ='/content/createAssignment'

        template_parms = {
        'courseId' : courseId,
        'uploadUrl': upload_url
        }



        self.render('content/content.html', **template_parms)

class CreateAssignmentHandler(BaseRequestHandler):

    @decorator.oauth_required
    def post(self):
        try:
            id = self.request.POST.get('courseId')
            assTitle = self.request.POST.get('assTitle')
            assDescription = self.request.POST.get('assDescription')
            workTypes = self.request.POST.get('workTypes')
            fileUrl = self.request.POST.get('fileUrl')



            course_work = {
                'title' : assTitle,
                'description' : assDescription,
                'workType' : workTypes,
                'state': "PUBLISHED",
                'materials': { 'link': { 'url': fileUrl }}
            }


            course_work = service.courses().courseWork().create(courseId=id, 
                                                                body=course_work).execute(http=decorator.http())


        except client.AccessTokenRefreshError:
            print "ERROR" * 80