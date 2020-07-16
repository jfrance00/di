import flask
import flask_wtf
import wtforms as wtf
import json
from . import inventory

with open(inventory, 'rb') as f:
    data = json.load(f)


class Location(flask_wtf.FlaskForm):
    city = wtf.SelectField('Location:', choices=['New York', 'Paris', 'Tel Aviv']) #to improve: find way to make choices
    submit = wtf.SubmitField('Submit')                                             # dynamic according to the JSON file


class CustomerItem(flask_wtf.FlaskForm):
    size = wtf.SelectField('Size', choices=['5', '6', '7'])
    color = wtf.SelectField('color', choices=['blue', 'red', 'black'])
    submit = wtf.SubmitField('Add to Cart')


