from src.framework.request_handler import BaseRequestHandler


class CreateCourse(BaseRequestHandler):
    def get(self):


        template_parms = {
        }

        self.render('course/createCourse.html', **template_parms)


