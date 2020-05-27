import os
import json

from flask import Blueprint
from flask import render_template, redirect, url_for
from flask import send_file, send_from_directory
from flask import Response, json

from flask import request
from flask_restful import Resource

from flask_login import login_required
from flask_login import current_user

from .forms import addForm
from .models import Todo
from app.extensions import db, api
from app.settings import CLIENT_IMAGES

from flask.views import MethodView


class TodoView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page, 10).items
            res = {}
            for product in products:
                res[product.id] = {
                    'name': product.name,
                    'price': str(product.price),
                }
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name': product.name,
                'price': str(product.price),
            }
        return jsonify(res)
 
    def post(self):
        name = request.form.get('name')
        price = request.form.get('price')
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'name': product.name,
            'price': str(product.price),
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return




blueprint = Blueprint('main', __name__, template_folder='templates', url_prefix='/main', static_folder='static',static_url_path='/static/')


@blueprint.route("/get-image/<image>",methods=["GET"])
@login_required
def getImage(image):
    try:
        return send_from_directory(CLIENT_IMAGES, filename=image, mimetype='image/jpg', as_attachment=True) #attachment_filename='avatar.jpg',
    except FileNotFoundError:
        return abort(404)


@blueprint.route('/')
@login_required
def index():

    form = addForm()
    if form.validate_on_submit():
        todo = Todo(
            form.title.data,
            form.description.data,
            form.date_at.data,
            current_user.id
        )
        db.session.add(todo)
        db.session.commit()
        resp = Response( json.dumps({"status":"success","msg":"save successfull",})  , status=200, mimetype='application/json' )
        return resp

    avatar = True if os.path.exists(os.path.join(CLIENT_IMAGES, '{}.jpg'.format(current_user.id))) else False
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('main.html', todos=todos, user=current_user, form=form, avatar = avatar, title="Tasks to do")


@blueprint.route('/add', methods=["GET", "POST"])
@login_required
def addTodo():

    form = addForm()
    if form.validate_on_submit():
        todo = Todo(
            form.title.data,
            form.description.data,
            form.date_at.data,
            current_user.id
        )
        db.session.add(todo)
        db.session.commit()
        resp = Response( json.dumps({"status":"success","msg":"saved successfull",})  , status=200, mimetype='application/json' )
        return resp
    resp = Response( json.dumps({"status":"error","msg":"Error",})  , status=200, mimetype='application/json' )
    return resp


@blueprint.route('/delete/<int:id>')
@login_required
def delTodo(id):
    
    task = Todo.query.filter_by(tasks=current_user,id=id).first()
    if task is None:
        resp = Response( json.dumps({"status":"error","msg":"dont allowed"})  , status=200, mimetype='application/json' )
        return resp
    else:
        db.session.delete(task)
        db.session.commit()
        resp = Response( json.dumps({"status":"success","msg":"deleted successfull",'remove':True,"id":id})  , status=200, mimetype='application/json' )
        return resp



class StickyNotes(Resource):

    def get(self, id=None, page=1):
        if not id:
            todos = Todo.query.filter_by(tasks=current_user).paginate(page, 10).items
            res = {}
            for todo in todos:
                res[todo.id] = {
                    'title': todo.title,
                    'description': todo.description,
                    'date_at': str(todo.date_at),
                }
        else:
            todo = Todo.query.filter_by(id=id).first()
            if not todo:
                abort(404)
            res = {
                'title': todo.title,
                'description': todo.description,
                'date_at': str(todo.date_at),
            }
        return jsonify(res)

 
    def post(self):
        name = request.form.get('name')
        price = request.form.get('price')
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'name': product.name,
            'price': str(product.price),
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):

        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Delete the record for the provided id.
        return

api.add_resource(StickyNotes, '/api/v1/', endpoint='main')
api.add_resource(StickyNotes, '/api/v1/<int:id>', endpoint='main')
