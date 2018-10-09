from src.models.baseModel import BaseModel, decorator, client, service, ndb


class Announcement(BaseModel):

    title = ndb.StringProperty(default=None)
    content = ndb.StringProperty(default=None)
    timestamp = ndb.DateTimeProperty(auto_now=True)
    ownerId = ndb.StringProperty(default=None)
    courseId = ndb.StringProperty(default=None)
    ownerEmail = ndb.StringProperty(default=None)

    @staticmethod
    def get_by_courseID(id):
        query = Announcement.query(Announcement.courseId == id)
        return query.fetch()

    
