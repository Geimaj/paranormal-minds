from webapp2 import WSGIApplication
from webapp2 import Route


app = WSGIApplication(
    routes=[
        Route('/', handler='src.app.home.Home'),
        Route('/announcements', handler='src.app.announcements.Announcements'),
        Route('/course/create', handler='src.app.createCourse.CreateCourse'),
        Route('/course/join', handler='src.app.joinCourse.JoinCourse')
    ]
)

