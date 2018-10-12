from src.framework.api import service, decorator, users
from src.framework.request_handler import BaseRequestHandler

from google.appengine.runtime import DeadlineExceededError

import src.models as models


class Discussion(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseID):


        template_parms = {
            'courseID': courseID
        }

        self.render('discussion/discussion.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseID):
        # get data from form
        topic = self.request.POST.get('topic')
        description = self.request.POST.get('description')

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
        discussionTopic.courseId = courseID

        # save DiscussionTopic Object to DB
        discussionTopic.put()

        self.redirect('/course/%s' % courseID)
