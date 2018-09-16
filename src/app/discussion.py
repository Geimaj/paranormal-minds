from src.framework.request_handler import BaseRequestHandler


class Discussion(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('discussion/discussion.html', **template_parms)

    def post(self):
        {

        }
