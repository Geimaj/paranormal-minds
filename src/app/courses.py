from src.framework.request_handler import BaseRequestHandler
import src.models as models
from src.framework.api import decorator, service

class CoursesHandler(BaseRequestHandler):

    @decorator.oauth_required
    def get(self):

        # courses = models.Course.getCourses()
        courses = service.courses().list(courseStates=['ACTIVE', 'PROVISIONED', 'ARCHIVED']).execute(decorator.http())

        template_parms = {
            'title': 'My Courses',
            'courses': courses['courses']
        }

        self.render('course/courses.html', **template_parms)
