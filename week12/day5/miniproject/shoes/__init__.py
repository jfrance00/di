import flask

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

inventory = "inventory.json"

from . import views
