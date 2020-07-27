import flask

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

user_database = 'users.json'

from . import views
