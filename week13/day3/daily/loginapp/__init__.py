import flask
import flask_sqlalchemy
import flask_login
import flask_migrate
import os

# login_manager = flask_login.LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

user_database = 'users.json'

# login_manager.init_app(app)

from . import views
