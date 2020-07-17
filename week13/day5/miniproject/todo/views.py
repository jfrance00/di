import flask

from . import app, db
from . import models

@app.route('/', methods=('GET', 'POST'))
def index():
    if flask.request.method == 'POST':
        todo = flask.request.form['todo']

        task = models.Todo(todo=todo)
        db.session.add(task)
        db.session.commit()
        print('add task to db')


    return flask.render_template('index.html')
