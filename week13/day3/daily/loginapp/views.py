import flask
import json
import os

from . import forms
from . import app, user_database #login_manager


@app.route("/", methods=['GET', 'POST'])
def home():
    basedir = os.path.abspath(os.path.dirname(__file__))
    form = forms.CheckName()
    with open('users.json', 'rb') as user_db:
        data = json.load(user_db)
    if flask.request.method == 'POST':
        name = form.name.data
        user = {"name": name}
        known_user = False
        for item in data["users"]:
            if item['name'].lower() == name.lower():
                known_user = True
                flask.flash(f'{name} already registered, please login', 'info')
        if not known_user:
            flask.flash(f'{name} is not registered. Please sign up')


    else:
        pass
    return flask.render_template('home.html', form=form, data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return flask.render_template('login.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUp()
    return flask.render_template('sign-up.html', method=['GET', 'POST'])
