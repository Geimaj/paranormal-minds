from src.framework.request_handler import BaseRequestHandler


class Content(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('content/content.html', **template_parms)

    def post(self):
        {

        }
