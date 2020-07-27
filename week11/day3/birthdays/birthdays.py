import flask
import json

app = flask.Flask(__name__)

@app.route('/home')
def home():
    return flask.render_template('home.html')

@app.route('/add-user/<str: age')
def add_user(age):
    return flask.render_template()