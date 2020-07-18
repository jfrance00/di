import flask
import flask_sqlalchemy
# import flask_migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "SQLITE:////" + os.path.join(basedir, 'app.db')
app.config['SECRET_KEY'] = 'blahblah'
db = flask_sqlalchemy.SQLAlchemy(app)
# migrate = flask_migrate.Migrate(app, db)

from . import views, models
db.create_all()


