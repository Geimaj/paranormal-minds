from google.appengine.ext import ndb
from src.framework.api import decorator, service, client

class BaseModel(ndb.Model):
    @staticmethod
    def test():
        print 'test'
