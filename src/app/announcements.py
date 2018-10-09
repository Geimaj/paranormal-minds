# import request handler
from src.framework.request_handler import BaseRequestHandler

# import utils for api access
from src.framework.api import service, decorator

# import our models
import src.models as models

#import google users api
from google.appengine.api import users


class Announcements(BaseRequestHandler):

    @decorator.oauth_required
    def get(self, courseId):

        # get course object based on the id that came from the url
        course = models.Course.get_by_id(courseId)
        
        # pass course object to template so we can pull data from it
        template_parms = {
            'course': course
        }

        # render the template and pass the params
        self.render('announcements/announcements.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseId):

        # get data from form
        # based on the name of the input element in the form 
        title = self.request.POST.get('title')
        description = self.request.POST.get('description')          

        #get current user
        user = users.get_current_user()
        # get id of user
        ownerId = user.user_id()
        email = user.email()

        # create announcement object from our models
        announcement = models.Announcement()

        # pass data to announcemnt object
        announcement.title = title
        announcement.content = description
        announcement.courseId = courseId
        announcement.ownerId = ownerId
        announcement.ownerEmail = email

        # write to db
        announcement.put()

        # redirect back to course page
        self.redirect('/course/%s' % courseId)


        


