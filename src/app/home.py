from src.framework.request_handler import BaseRequestHandler


class Home(BaseRequestHandler):
    def get(self):

        template_parms = {
        }

        self.render('home/home.html', **template_parms)