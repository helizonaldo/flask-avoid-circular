from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_login import current_user

blueprint = Blueprint("public",__name__, template_folder='templates', static_folder='static',static_url_path="/static/public/")


@blueprint.route("/")
def index():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	else:
		return render_template('index.html')
		