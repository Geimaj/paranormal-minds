from src.framework.api import service, decorator, users
from src.framework.request_handler import BaseRequestHandler, jinja2

#import google users api
from google.appengine.api import users

import src.models as models


class Discussion(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseId):

        course = models.Course.get_by_id(courseId)

        template_parms = {
            'course': course
        }

        self.render('discussion/discussion.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseId):
        # get data from form
        topic = self.request.POST.get('topic')
        topic = jinja2.escape(topic)
        description = self.request.POST.get('description')
        description = jinja2.escape(description)

        userProfile = users.get_current_user()
        userId = userProfile.user_id()


        email = userProfile.email()

        # create DiscussionTopic object
        discussionTopic = models.DiscussionTopic()

        # pass in data from form
        discussionTopic.title = topic
        discussionTopic.description = description
        discussionTopic.ownerId = userId
        discussionTopic.ownerEmail = email
        discussionTopic.courseId = courseId

        # save DiscussionTopic Object to DB
        discussionTopic.put()

        
        # create announcement object from our models
        announcement = models.Announcement()

        # pass data to announcemnt object
        announcement.title = topic
        announcement.content = description
        announcement.courseId = courseId
        announcement.ownerId = userId
        announcement.ownerEmail = email

        # write to db
        announcement.put()

        self.redirect('/course/%s' % courseId)
