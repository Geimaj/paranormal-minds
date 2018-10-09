
from webapp2 import WSGIApplication
from webapp2 import Route

from src.framework.api import decorator

app = WSGIApplication(
    routes=[
        Route('/', handler='src.app.home.Home'),
        Route('/announcements', handler='src.app.announcements.Announcements'),
        Route('/course/create', handler='src.app.course.CreateCourse'),
        Route('/course/join', handler='src.app.course.JoinCourse'),
        Route('/course/<id>', handler='src.app.course.CourseHandler'),
        Route('/courses', handler='src.app.courses.CoursesHandler'),
        Route('/content/createAssignment', handler='src.app.content.CreateAssignmentHandler'),
        Route('/content/<courseId>', handler='src.app.content.ContentHandler'),
        Route(decorator.callback_path, decorator.callback_handler()),

    ]
)

