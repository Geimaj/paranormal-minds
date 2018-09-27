from src.framework.request_handler import BaseRequestHandler
from google.appengine.api import users

class Home(BaseRequestHandler):
    def get(self):

        user = users.get_current_user()

        template_parms = {
            'user': user
        }

        self.render('home/home.html', **template_parms)