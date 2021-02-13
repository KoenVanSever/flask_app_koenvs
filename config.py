# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - SQLITE3
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
if os.environ["SQLALCHEMY_DATABASE_URI"]:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, os.environ["SQLALCHEMY_DATABASE_URI"])
DATABASE_CONNECT_OPTIONS = {}

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "qfdsqncx135q5313qdswfqrg4153h1qd3qd1f5q3"

# Secret key for signing cookies
SECRET_KEY = "qs351qdqsdhhtfsibd4153q1q'qd5g4153q"

# Configure permanent session lifetime when permanent session is True
from datetime import timedelta
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

USE_SESSION_FOR_NEXT = True
