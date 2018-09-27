from webapp2 import RequestHandler
import jinja2
import os

#google libs
from google.appengine.api import users

#custom libs
from src.framework import api
from src.models import course


class BaseRequestHandler(RequestHandler):
    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        "templates")

    jinja_enviroment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir)
    )

    def render(self, template, **kwargs):
        jinja_template = self.jinja_enviroment.get_template(template)

        nickname = ''
        logout_url = ''
        login_url = ''
        enrolled_courses = []

        user = users.get_current_user()
        if (user):
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            enrolled_courses = course.getCourses()

            print '_='*20
            print enrolled_courses
            print '_='*20

        else:
            login_url = users.create_login_url('/')


        kwargs['username'] = nickname
        kwargs['logout_url'] = logout_url
        kwargs['login_url'] = login_url
        kwargs['enrolled_courses'] = []#enrolled_courses

        template_html = jinja_template.render(kwargs)

        self.response.out.write(template_html)



    # #TODO: MOVE THIS
    # @decorator.oauth_required
    # def getCourses(self):
    #     # Call the Classroom API
    #     print 'GET COURSES'
    #     try:
    #         results = service.courses().list(pageSize=10).execute(http=decorator.http())

    #         # print'/|'*30
    #         # print results
    #         # print'/|'*30

    #         # if results:
    #         #     enrolled_courses = results.get('courses', [])
    #         #     return  enrolled_courses

    #     except client.AccessTokenRefreshError as e:
    #         print 'CLIENT ACCESS TOKEN REFRESH ERROR'
    #         print e
    #         # self.redirect('/')