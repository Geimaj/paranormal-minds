from src.models.baseModel import BaseModel, decorator, client, service


class Course(BaseModel):

    @staticmethod
    def get_by_id(id):
        if decorator.has_credentials():
            course = service.courses().get(id=id).execute(http=decorator.http())
            return course
        else:
            print 'NING CRED'    

    @staticmethod
    def getCourses():
        # has user authenticated api access
        if decorator.has_credentials():
            # Call the Classroom API
            try:
                results = service.courses().list(pageSize=10).execute(http=decorator.http())
                enrolled_courses = results.get('courses', [])
                return enrolled_courses
            except client.AccessTokenRefreshError as e:
                print 'CLIENT ACCESS TOKEN REFRESH ERROR'
                print e
        else:
            print 'no cred'
        return None

    @staticmethod
    def isUserTeacher(courseID, userID):
        if decorator.has_credentials():
            try:
                # get teachers for courseID
                results = service.courses().teachers().list(courseId=courseID).execute(decorator.http())
                teachers = []
                if results['teachers']:
                    teachers = results['teachers']

                for teacher in teachers:
                    # yes that userID is a teacher for that courseID
                    if teacher['userId'] == userID:
                        #stop looking and return true
                        return True

                #we didnt find any matching ID so this userID is not a teacher
                return False

            except Exception as e:
                print e
        else:
            print
            print 'NO CRED'
            print
