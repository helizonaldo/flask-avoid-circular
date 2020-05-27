import datetime as dt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True, index=True)
    username = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    is_admin = db.Column(db.Boolean(), default=False)    
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.now) #dt.datetime.utcnow
    last_seen = db.Column(db.DateTime, nullable=True, default=dt.datetime.now)
    todos = db.relationship('Todo',backref='tasks',lazy='dynamic')

    def __init__(self, username, email, password, **kwargs):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


    def checkPassword(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):  
        return f"<username={self.username}>"

