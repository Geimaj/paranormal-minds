from src.framework.api import service, decorator
from src.framework.request_handler import BaseRequestHandler

from google.appengine.runtime import DeadlineExceededError


class Discussion(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('discussion/discussion.html', **template_parms)

    def post(self):
        {

        }

class AddDiscussion(BaseRequestHandler):

    def post(self):
        try:
            message = self.request.POST.get('message')


            discussion =  {
                'Usermessage': message,
            }

            self.response.out.write(message)

            # discussion = service.discussion().create(body=discussion).execute(http=decorator.http())
            # self.redirect('/' + discussion.id)

        except DeadlineExceededError as e:
            print 'EXPECTION' * 20
            print e

        print"fuck you"
