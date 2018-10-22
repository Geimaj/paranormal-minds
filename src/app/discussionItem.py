from src.framework.api import service, decorator, users
from src.framework.request_handler import BaseRequestHandler, jinja2

#import google users api
from google.appengine.api import users
from google.appengine.ext import ndb


import src.models as models


class DiscussionItem(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, discussionTopicID):

        discussionItems = []
        discussionTopic = None
        
        try:

            discussionTopic = models.DiscussionTopic.get_by_id(int(discussionTopicID))
            discussionItemsQuery = models.DiscussionItem.query(models.DiscussionItem.discussionTopicId == str(discussionTopicID))
            results = discussionItemsQuery.order(+models.DiscussionItem.timestamp).fetch()
            
            print results

            discussionItems = results

        except Exception as e:
            print 'error fetching items or topics '
            print e

        template_parms = {
            'discussionTopic': discussionTopic,
            'discussionItems': discussionItems
        }

        self.render('discussion/courseDiscussion.html', **template_parms)

    @decorator.oauth_required
    def post(self, discussionTopicID):
        # get data from form
        uMessage = self.request.POST.get('uMessage')

        uMessage = jinja2.escape(uMessage)

        userProfile = users.get_current_user()
        userId = userProfile.user_id()


        email = userProfile.email()

        # create DiscussionTopic object
        discussionItem = models.DiscussionItem()

        # pass in data from form
        discussionItem.content = uMessage
        discussionItem.ownerId = userId
        discussionItem.ownerEmail = email
        discussionItem.discussionTopicId = discussionTopicID 

        # save DiscussionTopic Object to DB
        discussionItem.put()

        self.redirect('/courseDiscussion/%s#messageText' % discussionTopicID)
