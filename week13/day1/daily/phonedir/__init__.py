import flask
import flask_sqlalchemy
import flask_migrate
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)
db = flask_sqlalchemy.SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = flask_sqlalchemy.SQLAlchemy(app)

migrate = flask_migrate.Migrate(app, db)
app.config['SECRET_KEY'] = "itsasecret"

from . import views, models

db.create_all()

