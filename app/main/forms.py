import datetime as dt
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

from .models import Todo

class addForm(FlaskForm):
    title = StringField('Title', validators=[ DataRequired("Title is required"), Length(max=64) ] )
    description = StringField('Message', validators=[ DataRequired("Message is required"), Length(max=200) ] )
    date_at = DateTimeField("Date", default=dt.datetime.now, validators=[DataRequired()])

