import flask
import wtforms as wtf
from . import forms, models
from . import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SearchInput()
    return flask.render_template('index.html', form=form)


@app.route('/add-input', methods=['GET', 'POST'])
def add_input():
    form = forms.AddToDatabase()
    if flask.request.method == "POST":
        id = form.id.data
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        address = form.address.data
        entry = models.Person(id=id, name=name, phone=phone, email=email, address=address)
        db.session.add(entry)
        db.session.commit()
        flask.flash(f'{name} added successfully')
    return flask.render_template('add-input.html', form=form)