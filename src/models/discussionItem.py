from src.models.baseModel import BaseModel, decorator, client, service, ndb


class DiscussionItem(BaseModel):

    discussionTopictId = ndb.StringProperty(default=None)
    content = ndb.StringProperty(default=None)    
    timestamp = ndb.DateTimeProperty(auto_now=True)
    ownerId = ndb.StringProperty(default=None)
    ownerEmail = ndb.StringProperty(default=None)


    
