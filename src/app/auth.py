from src.framework.request_handler import BaseRequestHandler, decorator


class AuthEnable(BaseRequestHandler):
    #display page explaining why auth is needed
    def get(self):

        template_parms = {
        }

        self.render('auth/authorize.html', **template_parms)

    #handle auth and redirect back to home
    @decorator.oauth_required
    def post(self):
        self.redirect('/')
