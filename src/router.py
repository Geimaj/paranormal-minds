
from webapp2 import WSGIApplication
from webapp2 import Route

from src.framework.api import decorator

app = WSGIApplication(
    routes=[
        Route('/', handler='src.app.home.Home'),
        Route('/announcements/create/<courseId>', handler='src.app.announcements.Announcements'),
        Route('/announcements', handler='src.app.announcements.Announcements'),
        
        Route('/discussion/create/<courseId>', handler='src.app.discussion.Discussion'),
        Route('/discussion', handler='src.app.discussion.Discussion'),

        Route('/courseDiscussion/<discussionTopicID>', handler='src.app.discussionItem.DiscussionItem'),
        Route('/courseDiscussion', handler='src.app.discussionItem.DiscussionItem'),
        
        Route('/course/create', handler='src.app.course.CreateCourse'),
        Route('/course/join', handler='src.app.course.JoinCourse'),
        Route('/course/<courseID>/details', handler='src.app.course.CourseDetailsHandler'),
        Route('/course/<courseID>/leave', handler='src.app.course.LeaveCourseHandler'),
        Route('/course/<courseID>/remove', handler='src.app.course.RemoveStudentHandler'),
        Route('/course/<id>', handler='src.app.course.CourseHandler'),
        
        Route('/courses', handler='src.app.courses.CoursesHandler'),
        
        Route('/content/createAssignment', handler='src.app.content.CreateAssignmentHandler'),
        Route('/content/submission', handler='src.app.content.SubmissionHandler'),
        Route('/content/<courseId>', handler='src.app.content.ContentHandler'),

        Route('/invite/student/<courseID>', handler='src.app.invite.StudentInviteHandler'),
        Route('/invite/teacher/<courseID>', handler='src.app.invite.TeacherInviteHandler'),
        
        
        
        Route(decorator.callback_path, decorator.callback_handler()),

    ]
)

