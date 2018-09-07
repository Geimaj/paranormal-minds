from webapp2 import WSGIApplication
from webapp2 import Route


app = WSGIApplication(
    routes=[
        Route('/', handler='src.app.home.Home'),
        Route('/course/create', handler='src.app.createCourse.CreateCourse'),
        Route('/content/content', handler='src.app.content.Content'),
        Route('/discussion/discussion', handler='src.app.discussion.Discussion'),
        Route('/announcements', handler='src.app.announcements.Announcements')
    ]
)

