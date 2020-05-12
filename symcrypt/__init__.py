import importlib
import inspect

from flask import Flask, session, g, request, jsonify, abort, url_for
from flask_login import LoginManager, login_user
from flask_restful import Api

from mongoengine import connect
from symcrypt.user.models import UserModel
from symcrypt.conf import MONGO_HOST, MONGO_PORT, SECRET_KEY, INSTALLED_MODULES


connect('symcrypt', host=MONGO_HOST, port=MONGO_PORT)


app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

api = Api(app)


@login_manager.user_loader
def load_user(user):
    return UserModel.objects(username=user).first()


@app.route("/user/reset_password", methods=['GET', 'POST'])
def reset_pass():
    u = UserModel.objects(username=request.form['username'])
    if u is None:
        flash('That username is an invalid ')
        return redirect(url_for('/user/login'))
    hashed_password = request.form['password'] 
    User.objects(username=u.username).update_one(password=hashed_password)
    flash('Your password has been updated! You are now able to log in', 'success')
    return redirect(url_for('/user/login'))


@app.route('/user/login', methods=['POST'])
def login():
    u = UserModel.objects(username=request.form['username']).first()
    if u:
        if u.password == request.form['password']:
            login_user(u) 
            return jsonify(
                {
                    'err': '',
                }
            ), 200
        else:
            return jsonify(
                {
                    'err': 'username or password is not correct',
                }
            ), 400
    else:
        return jsonify(
            {
                'err': 'the user does not exist'
            }
        ), 404


for pkg in INSTALLED_MODULES:
    service_script = importlib.import_module(
        "symcrypt.%s.resources" % pkg)
    admin_script = importlib.import_module('symcrypt.%s.models' % pkg)
    for name, obj in inspect.getmembers(service_script):
        if inspect.isclass(obj) and 'symcrypt.%s' % pkg in str(obj) and 'Resource' in str(obj):
            api.add_resource(
                obj,
                '/%s/%s' % (pkg, obj.url),
                endpoint='%s.%s' % (pkg, obj.__name__)
            )
    for name, obj in inspect.getmembers(admin_script):
        if inspect.isclass(obj) and 'api.%s' % pkg in str(obj) and 'Model' in str(obj):
            admin.add_view(ModelView(obj))
