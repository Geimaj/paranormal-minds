from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication(
    routes=[
        Route('/', handler='app.home.Home'),
        Route('/announcements', handler='app.announcements.Announcements'),
        Route('/course/create', handler='app.createCourse.CreateCourse')
    ]
)

