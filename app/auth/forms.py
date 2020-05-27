from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

from .models import User

class SignupForm(FlaskForm):
    username = StringField('Nome', validators=[ DataRequired("Nome é Obrigatorio"), Length(max=64) ] )
    password = PasswordField('Password', validators=[DataRequired("Senha Obrigatoria"),  Length(5,30,"A senha deve ter no minimo 5 caracteres")])
    email = EmailField('Email', validators=[DataRequired("Email obrigatorio"), Email("Email invalido")])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email2 = EmailField()
    email = EmailField('Email', validators=[DataRequired("Email obrigatorio"),Email("Email invalido")])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')