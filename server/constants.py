"""App constants"""

STUDENT_ROLE = 'student'
GRADER_ROLE = 'grader'
STAFF_ROLE = 'staff'
INSTRUCTOR_ROLE = 'instructor'
VALID_ROLES = [STUDENT_ROLE, GRADER_ROLE, STAFF_ROLE, INSTRUCTOR_ROLE]
STAFF_ROLES = [GRADER_ROLE, STAFF_ROLE, INSTRUCTOR_ROLE]
GRADE_TAGS = ['composition', 'correctness', 'total', 'partner a', 'partner b',
              'regrade', 'revision']
API_PREFIX = '/api'
OAUTH_SCOPES = ['all', 'email']

COURSE_ENDPOINT_FORMAT = '^\w+/\w+/\w+$'
ASSIGNMENT_ENDPOINT_FORMAT = COURSE_ENDPOINT_FORMAT[:-1] + '/\w+$'

GRADES_BUCKET = 'ok_grades_bucket'
TIMEZONE = 'America/Los_Angeles'
ISO_DATETIME_FMT = '%Y-%m-%d %H:%M:%S'

AUTOGRADER_URL = 'https://autograder.cs61a.org'

FORBIDDEN_ROUTE_NAMES = [
    'about',
    'admin',
    'api',
    'comments',
    'login',
    'logout',
    'oauth',
    'testing-login',
]
FORBIDDEN_ASSIGNMENT_NAMES = []
