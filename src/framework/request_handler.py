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
        loader=jinja2.FileSystemLoader(template_dir))

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
        else:
            login_url = users.create_login_url('/')


        kwargs['username'] = nickname
        kwargs['logout_url'] = logout_url
        kwargs['login_url'] = login_url
        kwargs['enrolled_courses'] = []#enrolled_courses

        template_html = jinja_template.render(kwargs)

        self.response.out.write(template_html)

    @staticmethod
    def getKeyFromData(data,key):
        if key in data.keys():
            return data[key]
        return []
