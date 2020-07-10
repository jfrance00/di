import flask
import json
from . import forms
from . import app, inventory


@app.route("/", methods=['GET', 'POST'])
def home():
    form = forms.Location()
    if flask.request.method == "POST":
        city = form.city.data
        print(city)
        return flask.redirect(flask.url_for('main', city=city))
    else:
        return flask.render_template('home.html', form=form)

@app.route('/main/<city>', methods=['GET', 'POST'])
def main(city):
    with open(inventory, 'rb') as f:
        data = json.load(f)
        return flask.render_template('main.html', data=data, city=city)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return flask.render_template('cart.html')

