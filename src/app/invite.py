from src.framework.request_handler import BaseRequestHandler
from src.framework.api import service, decorator

class StudentInviteHandler(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseID):

        template_parms = {
            'courseID': courseID,
            'inviteType': 'student'            
        }

        self.render('invite/invite.html', **template_parms)
        
    @decorator.oauth_required
    def post(self, courseID):

        # get data from form
        email = self.request.POST.get('email')

        student = {
            'userId': email,
            'courseId': courseID,
            'role': 'STUDENT'
        }

        try:

            # create invite object
            invite = service.invitations().create(body=student).execute(http=decorator.http())

            self.redirect('/course/%s' % courseID)
        except Exception as e:
            print e


class TeacherInviteHandler(BaseRequestHandler):
    @decorator.oauth_required
    def get(self, courseID):

        template_parms = {
            'title': 'Invite',
            'courseID': courseID,
            'inviteType': 'teacher'
        }

        self.render('invite/invite.html', **template_parms)
        
    @decorator.oauth_required
    def post(self, courseID):

        # get data from form
        email = self.request.POST.get('email')

        teacher = {
            'userId': email,
            'courseId': courseID,
            'role': 'TEACHER'
        }

        try:
            # create invite object
            invite = service.invitations().create(body=teacher).execute(http=decorator.http())

            self.redirect('/course/%s' % courseID)
        except Exception as e:
            print e