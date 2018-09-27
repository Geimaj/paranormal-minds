
from webapp2 import WSGIApplication
from webapp2 import Route

from src.framework.request_handler import decorator

app = WSGIApplication(
    routes=[
        Route('/', handler='src.app.home.Home'),
        Route('/announcements', handler='src.app.announcements.Announcements'),
        Route('/course/create', handler='src.app.createCourse.CreateCourse'),
        Route('/course/join', handler='src.app.joinCourse.JoinCourse'),
        Route('/course/<id>', handler='src.app.course.CourseHandler'),
        Route(decorator.callback_path, decorator.callback_handler()),
        Route('/auth/enable', handler='src.app.auth.AuthEnable'),

    ]
)

