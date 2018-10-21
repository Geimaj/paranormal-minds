from src.models.baseModel import BaseModel, decorator, client, service, ndb
from src.models import discussionItem

class DiscussionTopic(BaseModel):

    title = ndb.StringProperty(default=None)
    description = ndb.StringProperty(default=None)    
    timestamp = ndb.DateTimeProperty(auto_now=True)
    ownerId = ndb.StringProperty(default=None)
    courseId = ndb.StringProperty(default=None)
    ownerEmail = ndb.StringProperty(default=None)

    def getDiscussionItems(self):
        items = discussionItems.query().fetch()

    # @staticmethod
    # def get_by_id(id):
    #     return DiscussionTopic.query(DiscussionTopic.key.id() == id).fetch()
        

    

    