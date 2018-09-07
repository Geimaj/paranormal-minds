from webapp2 import RequestHandler
import os
import jinja2

from google.appengine.api import users


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

        user = users.get_current_user()
        if (user):
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
        else:
            login_url = users.create_login_url('/')

        kwargs['username'] = nickname
        kwargs['logout_url'] = logout_url
        kwargs['login_url'] = login_url

        template_html = jinja_template.render(kwargs)

        self.response.out.write(template_html)
