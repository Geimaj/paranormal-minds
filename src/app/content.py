import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity

from src.framework.request_handler import BaseRequestHandler
from src.framework.api import service, decorator, client



class ContentHandler(BaseRequestHandler):
    def get(self, courseId):

         template_parms = {
                'courseId' : courseId
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

            course_work = {
                'title' : assTitle,
                'description' : assDescription,
                'workType' : workTypes,
                'state': "PUBLISHED",
            }



            bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Demo GCS Application running from Version: '
                                + os.environ['CURRENT_VERSION_ID'] + '\n')
            self.response.write('Using bucket name: ' + bucket_name + '\n\n')            



            # course_work = service.courses().courseWork().create(courseId=id, body=course_work).execute(http=decorator.http())

            # self.response.out.write(course_work)

        except client.AccessTokenRefreshError:
            self.redirect('/')