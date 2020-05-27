from datetime import datetime

def init_app(app):

    def count_days(firstday):
        return (datetime.now() - firstday).days
    app.jinja_env.filters['countdays'] = count_days

    