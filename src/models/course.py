from src.framework.request_handler import decorator

@decorator.oauth_required
def getCourses():
    #has user authenticated api access
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
        #TODO: add link to page explaining why they should enable
        print 'no cred'
    return None