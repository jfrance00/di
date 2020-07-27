import flask
import json

from . import forms
from . import app, user_database


@app.route("/", methods=['GET', 'POST'])
def home():
    form = forms.CheckName()
    if flask.request.method == 'POST':
        fname = form.fname.data
        lname = form.lname.data
        user = {"fname": fname, "lname": lname}
        with open('users.json', 'rb'):
            data = json.load('users.json')
        for item in data:
            if fname == fname:
                print(item)
                flask.flash(f'{fname} already registered, please login')
            else:
                flask.flash(f'{fname} is not registered, please sign up')
    else:
        pass
    return flask.render_template('home.html', form=form, data=data)

#
# @app.route('/login', method=['GET', 'POST'])
# def login():
#     return flask.render_template('/login')
#
#
# @app.route('/sign-up', method=['GET', 'POST'])
# def sign_up():
#     return flask.render_template('/sign-up', method=['GET', 'POST'])
