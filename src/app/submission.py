import logging
import os

from google.appengine.api import app_identity
from apiclient.http import MediaFileUpload

from src.framework.request_handler import BaseRequestHandler
from src.framework.api import service, decorator, client, driveService

# import our models
import src.models as models

#import google users api
from google.appengine.api import users

class StudentSubmissionHandler(BaseRequestHandler):
    
    @decorator.oauth_required
    def get(self, courseID, courseWorkID):

        # get submissions for this courseWork id
        submission_results = service.courses().courseWork().studentSubmissions().list(courseId=courseID, courseWorkId=courseWorkID).execute(decorator.http())

        courseWork = service.courses().courseWork().get(id=courseWorkID, courseId=courseID).execute(decorator.http())
        
        course = service.courses().get(id=courseID).execute(decorator.http())

        submissions = self.getKeyFromData(submission_results, 'studentSubmissions')


        template_parms = {
            'title': "Submissions",
            'submissions': submissions,
            "course": course,
            'courseWork': courseWork
        }

        self.render('submission/submissions.html', **template_parms)