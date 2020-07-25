import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
test_db = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')

class Config(object):
	"""Base configuration for application."""
	DEBUG = False
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
	# Application threads. A common general assumption is
	# using 2 per available processor cores - to handle
	# incoming requests using one and performing background
	# operations using the other.
	THREADS_PER_PAGE = 2

	# Enable protection agains *Cross-site Request Forgery (CSRF)*
	CSRF_ENABLED     = True

	# Use a secure, unique and absolutely secret key for
	# signing the data. 
	CSRF_SESSION_KEY = "secret"

	# Secret key for signing cookies
	SECRET_KEY = "secret"

class DevConfig(Config):
	"""Dev configuration for application."""

	#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = test_db
	SQLALCHEMY_BINDS = {
	    'default': SQLALCHEMY_DATABASE_URI,
	    'readonly': test_db
	}

