from src.framework.api import service, decorator, users
from src.framework.request_handler import BaseRequestHandler

#import google users api
from google.appengine.api import users
from google.appengine.ext import ndb


import src.models as models


class DiscussionItem(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, discussionTopicID):

        # course = models.Course.get_by_id(courseId)

        discussion = 'api'

        discussionItems = []
        discussionTopic = None
        
        discussionTopic = models.DiscussionTopic.get_by_id("5275456790069248")
        # discussionTopic = ndb.Key(models.DiscussionTopic, '5275456790069248').get()
            # discussionItems = models.DiscussionItem.query().fetch()

        print
        print
        print
        print
        print

        print discussionTopic

        print
        print
        print
        print


        try:
            pass
        except Exception as e:
            print e


        template_parms = {
            'course': 'buthole',
            'discussionItem': discussionItems,
            'discussionTopic': discussionTopic
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
        # discussionItem.discussionTopicID = 

        # save DiscussionTopic Object to DB
        discussionItem.put()

        self.redirect('/course/%s' % courseId)
