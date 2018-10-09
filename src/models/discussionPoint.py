from src.models.baseModel import BaseModel, decorator, client, service, ndb


class discussionPoint(BaseModel):

    title = ndb.StringProperty(default=None)
    description = ndb.StringProperty(default=None)    
    timestamp = ndb.DateTimeProperty(auto_now=True)
    ownerId = ndb.StringProperty(default=None)
    courseId = ndb.StringProperty(default=None)
    ownerEmail = ndb.StringProperty(default=None)

    

    