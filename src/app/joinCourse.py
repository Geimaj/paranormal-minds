from src.framework.request_handler import BaseRequestHandler


class JoinCourse(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('course/joinCourse.html', **template_parms)

    def post(self):
        template_parms = {
        }

        self.render('course/joinCourse.html', **template_parms)

