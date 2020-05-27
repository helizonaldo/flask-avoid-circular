import datetime as dt
from app.extensions import db



class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(200), nullable=True)
	completed = db.Column(db.Boolean(), default=False)
	delayed = db.Column(db.Boolean(), default=False)
	created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.now)
	date_at = db.Column(db.DateTime, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
	
	@property
	def serialize(self):
		return{
			'id':self.id,
			'title':self.title,
			'description':self.description,
			'completed': self.completed,
			'delayed':self.delayed,
			'date_at':self.date_at,
			'user_id':self.user_id
		}

	def __init__(self, title, description , date_at, user_id):
		self.title = title
		self.description = description
		self.user_id= user_id

	def __repr__(self):  
		return f"<Todo {'%s','%s'}>" % (self.id, self.user_id)

