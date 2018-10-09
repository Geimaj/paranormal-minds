from google.appengine.ext import ndb
from src.framework.api import decorator, service, client

class BaseModel(ndb.Model):
	@staticmethod
	def fetch_single(query_obj):

		# Get all the accounts with that limit
		item_objs = query_obj.fetch(limit=1)

		# Did we get a account ?
		if item_objs != None and len(item_objs) > 0:

			# Return the first
			return item_objs[0]

		else: return None
