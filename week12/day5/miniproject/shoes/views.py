import flask
import json
from . import forms
from . import app, inventory


@app.route("/", methods=['GET', 'POST'])
def home():
    form = forms.Location()
    if flask.request.method == "POST":
        city = form.city.data
        return flask.redirect(flask.url_for('main', city=city))
    else:
        return flask.render_template('home.html', form=form)


@app.route('/main/<city>', methods=['GET', 'POST'])
def main(city):
    with open(inventory, 'rb') as f:
        data = json.load(f)
        return flask.render_template('main.html', data=data, city=city)


@app.route('/main/add-item/<city>/<item_id>', methods=['GET', 'POST'])
def add_item_details(city, item_id):
    order = forms.CustomerItem()
    with open(inventory, 'rb') as f:
        data = json.load(f)
     #here get the right sizes and colors according to the city and item#
    print(data['stores'].['city'])
    
    if flask.request.method == 'POST':
        order_choice = [order['size'], order['color']]
    return flask.render_template('item-page.html', data=data, city=city, item_id=item_id, order=order)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return flask.render_template('cart.html')

