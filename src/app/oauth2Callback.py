from src.framework.request_handler import BaseRequestHandler


class OauthCallbackHandler(BaseRequestHandler):


    def get(self):
        self.response.write('oauth handling...')
        state =  self.request.get('state')
        self.redirect(state)