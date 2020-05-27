import os
from datetime import timedelta     
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import smtplib, ssl

from flask import Blueprint
from flask import render_template, redirect, url_for
from flask import request
from flask import flash
from flask import Response, json

from flask_mail import Mail, Message

from flask_login import login_user, logout_user, login_required
from flask_login import current_user

from app.extensions import db, mail
from .models import User
from .forms import SignupForm, LoginForm


blueprint = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth', static_folder='static',static_url_path='/static/')
usts = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))

def valid_ip():
    client = request.remote_addr
    if client in ["10.86.6.5"]:
        return True
    else:
        return False




@blueprint.route('/login', methods=["GET", "POST"])
def signin():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():

    
        remember = form.remember.data
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash("Usuario ou senha inválida!",category="danger")
            return render_template("components/notifications.html") 

        if not user.checkPassword(form.password.data):
            flash("Usuario ou senha inválida!",category="danger")
            return render_template("components/notifications.html") 

       

        login_user(user, remember=remember,duration=timedelta(days=7))
        
        resp = Response( json.dumps({"redirect":"{}".format(url_for("main.index"))})  , status=200, mimetype='application/json' )
        return resp


    msg = "Login"
    return render_template('signin.html', form=form, title="Login", msg=msg)




@blueprint.route('/register', methods=["GET", "POST"])
def signup():
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))


    form = SignupForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email is None:
            user = User(
                form.username.data,
                form.email.data,
                form.password.data
            )
            db.session.add(user)
            db.session.commit()
        else:
            flash('email já cadastrado', category="danger")
            return render_template("components/notifications.html", clear=True) 

        flash('Cadastrado com sucesso!', category="success")
        return render_template("components/notifications.html")         


    return render_template('signup.html', form=form, title="Register")



@blueprint.route('/logout')
@login_required  
def logout():
    logout_user()
    return redirect(url_for('public.index'))



@blueprint.route('/account-recovery', methods=["GET", "POST"])
def passwordreset():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'GET':
        return render_template('passwordreset.html', title="Forgot you password!")

    email = request.form['email']
    token = usts.dumps(email, salt='email-confirm')
    msg = Message('Confirm Email', sender='noreply@example.com', recipients=[email])
    link = url_for('auth.confirm_email', token=token, _external=True)
    msg.html = render_template('emailnewpassword.html', link=link)    
    mail.send(msg)

    return render_template('passwordreset.html', sent=True , title="Password sent!")





@blueprint.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = usts.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'

    return render_template('changepassword.html', email="helizonaldo@hotmail.com", title="Change your password!")