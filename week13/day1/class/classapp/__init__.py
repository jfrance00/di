import flask
import flask_sqlalchemy
import flask_migrate
import os

#create variable to ROOT folder (abspath give absoolute path)
basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///"+"' #must be called like this, convention

db  = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

app.config['SECRET_KEY'] = 'secret'


from . import views