from src.models.baseModel import BaseModel, decorator, client, service


class Announcement(BaseModel):

    title = ndb.StringProperty(default=None)
    content = ndb.StringProperty(default=None)
    timestamp = ndb.DateTimeProperty(default=None)
    ownerId = ndb.StringProperty(default=None)
    courseId = ndb.StringProperty(default=None)

    
