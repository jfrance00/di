import flask
import flask_sqlalchemy
import flask_migrate
import os
from flask_login import UserMixin, current_user, login_user, logout_user

basedir = os.path.abspath(os.getcwd())

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secretsecret'

db = flask_sqlalchemy.SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")

migrate = flask_migrate.Migrate(app, db)

#------views----------

@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        role = flask.request.form['role']
        newuser = User(username=username, password=password, role=role)
        db.session.add(newuser)
        db.session.commit()
        flask.flash("user registered")
        print(newuser.username)
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == "POST":
        users = User.query.all()
        for item in users:
            username = flask.request.form['username']
            password = flask.request.form['password']
            user = User.query.filter_by(username=username).first()
            if username == user.username:
                print('username matches')
                if password == user.password:
                    print('password matches')
                    if user.role == "admin":
                        print('checking role in db')
                        return "admin page"
                    else:
                        return "user page"
                else:
                    flask.flash("login failed")
                    return flask.redirect(flask.url_for('index'))
            else:
                flask.flash("login failed")
                return flask.redirect(flask.url_for('index'))
    return flask.render_template('login.html')


@app.route('/admin')
def admin():
    return 'Admin'


@app.route('/user')
def user():
    return 'User'



#-----SQL class----------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70))
    password = db.Column(db.String(100))
    role = db.Column(db.String(15))

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


if __name__ == '__main__':
    app.run(debug=True)