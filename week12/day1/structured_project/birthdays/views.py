import flask
import json

from . import forms, models
from . import app, db

@app.route('/', methods=["GET", "POST"])
def index():

    form = forms.NewUserForm()
    if flask.request.method == "POST":
        name = form.name.data
        age = form.age.data

        # Create an object of a model:
        user = models.User(name=name, age=age)

        #user = {"name": name, "age": age, "msgs":[]}

        # Add this object to the database
        db.session.add(user) # --> Receives a db.Model object

        # Commit your changes on the database:
        db.session.commit()

        #if not open(database_fn, 'r').read():
        #    users = []
        #else:
        #    users = json.load(open(database_fn, 'r'))
        #users.append(user)
        #json.dump(users, open(database_fn, 'w'))

        flask.flash(f"User {name} registered !", category="success")
    else:
        messages = models.GreetingMessage.query.all()

    return flask.render_template("index.html", form=form, messages=messages)

@app.route('/add-user', methods=['GET', 'POST'])
def add_user_from_form():
    name = flask.request.form.get('username')
    age = flask.request.form.get('age')

    try:
        age = int(age)
        user = {"name": name, "age": age}
        if not open(database_fn, 'r').read():
            users = []
        else:
            users = json.load(open(database_fn, 'r'))
        users.append(user)
        json.dump(users, open(database_fn, 'w'))

        flask.flash(f"User {name} registered !", category="success")
    except:
        flask.flash("An error occured with the registration", category="error")


    return flask.redirect(flask.url_for('index'))

@app.route('/users')
def see_users():
    users = models.User.query.all()
    # users = json.load(open(database_fn, 'r'))
    return flask.render_template('users.html', user=user)

@app.route('/birthday-of-<username>')
def birthday(username):
    # can fetch only objects where field == value ==> models.User.query.filter_by(FIELD==VALUE)
    user = models.User.query.filter_by(name=username).first()
    print(f'found user {user}')
    #  users = json.load(open(database_fn, 'r'))
    # for user in users:
    #     if user['name'].lower() == username.lower():
    #         user['age'] += 1
    #         break

    json.dump(users, open(database_fn, 'w'))

    return flask.redirect(flask.url_for('see_users'))

# CREATE A VIEW: msg_to_user
# Send a form to the user with two fields: name and message
# Load the user with this name and append this message to his msgs list
@app.route("/msg-user/", methods=["GET", "POST"])
def msg_to_user():
    form = forms.NewMessageForm()

    if flask.request.method == "POST":
        name = form.name.data
        msg  = form.msg.data

        users = json.load(open(database_fn, 'r'))
        for user in users:
            if user['name'].lower() == name.lower():
                user['msgs'].append(msg)
                break

        json.dump(users, open(database_fn, 'w'))
        flask.flash(f"Sent a message to {name}")

        return flask.redirect(flask.url_for('index'))

    else:
        pass

    return flask.render_template("send_msg.html", form=form)


@app.route('/add-greeting', methods=['GET','POST'])
def add_greeting_message():
    form = forms.UserGreeting()
    if flask.request.method == 'POST':
        msg_obj = models.GreetingMessage(form.content.data)
        return flask.render_template(flask.url_for('index', msg_obj))

    return flask.render_template('add-greeting.html', form=form)