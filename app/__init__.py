import os
from flask import Flask, render_template

from app.settings import *
from app.extensions import db, migrate, login_manager, mail, api, admin
from app import auth, public, main, filters, adm as administrator


def create_app(config_object=os.environ['APP_SETTINGS']):
    app = Flask(__name__)
    app.config.from_object(config_object)    

    register_blueprints(app)
    register_errorhandlers(app)
    register_extensions(app)
    register_filters(app)
	
    return app


def register_blueprints(app):
    """Register Flask blueprints."""	
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(public.views.blueprint)    
    app.register_blueprint(main.views.blueprint)    
	
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.register_error_handler(errcode, render_error)

    return None


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    

    admin.init_app(app)    
    administrator.init_app(admin)

    api.init_app(main.views.blueprint)

    return None


def register_filters(app):
    filters.init_app(app)    
    return None