from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
api = Api()

