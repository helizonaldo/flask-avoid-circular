import os
import os.path

BASEDIR = os.path.abspath(os.path.dirname(__file__))
CLIENT_IMAGES = os.path.normpath(os.path.join(BASEDIR,'static/client/img'))

from abc import ABC  
class BaseConfig(ABC):
	DEBUG = False
	TESTING = False	
	SECRET_KEY = os.environ.get('SECRET_KEY')	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	FLASK_ADMIN_SWATCH = "cosmo"



	MAIL_SERVER = "smtp.gmail.com"
	MAIL_USERNAME =  os.environ.get('EMAIL_USER')
	MAIL_PASSWORD =  os.environ.get('EMAIL_PASSWORD')
	MAIL_PORT = 465 
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_DEFAULT_SENDER = "helizonaldo <helizonaldo@hotmail.com>"	


class DevelopmentConfig(BaseConfig):
	DEBUG = True

	SQLALCHEMY_DATABASE_URI = 'sqlite:///banco.db'

	MAIL_SERVER = "smtp.ethereal.email"
	MAIL_USERNAME = "logan.terry@ethereal.email"
	MAIL_PASSWORD = "cPadPVYrZtZY8yedYG"
	MAIL_PORT = 587 
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_DEFAULT_SENDER = "helizonaldo <helizonaldo@hotmail.com>"
	MAIL_DEBUG = True


class TestingConfig(BaseConfig):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///memory'

class ProductionConfig(BaseConfig):
    DEBUG = False

