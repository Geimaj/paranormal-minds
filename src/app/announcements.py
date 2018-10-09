from src.framework.request_handler import BaseRequestHandler


class Announcements(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('announcements/announcements.html', **template_parms)

    def post(self):
        {

        }
