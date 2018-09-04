from webapp2 import RequestHandler
import os
import jinja2


class BaseRequestHandler(RequestHandler):
    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        "templates")
    print 'TEMPLATE: ' + template_dir

    jinja_enviroment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir)
    )

    def render(self, template, **kwargs):
        jinja_template = self.jinja_enviroment.get_template(template)
        template_html = jinja_template.render(kwargs)

        self.response.out.write(template_html)
