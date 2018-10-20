from src.framework.api import service, decorator, users
from src.framework.request_handler import BaseRequestHandler

#import google users api
from google.appengine.api import users



import src.models as models


class DiscussionItem(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseId):

        course = models.Course.get_by_id(courseId)

        discussionItem = []

        try:
            discussionItem = models.DiscussionItem.query().fetch()
        except Exception as e:
            print e


        template_parms = {
            'course': course,
            'discussionItem': discussionItem
        }

        self.render('discussion/courseDiscussion.html', **template_parms)

    @decorator.oauth_required
    def post(self, courseId):
        # get data from form
        uMessage = self.request.POST.get('uMessage')

        userProfile = users.get_current_user()
        userId = userProfile.user_id()


        email = userProfile.email()

        # create DiscussionTopic object
        discussionItem = models.DiscussionItem()

        # pass in data from form
        discussionItem.content = uMessage
        discussionItem.ownerId = userId
        discussionItem.ownerEmail = email
        discussionItem.courseId = courseId

        # save DiscussionTopic Object to DB
        discussionItem.put()

        self.redirect('/course/%s' % courseId)
