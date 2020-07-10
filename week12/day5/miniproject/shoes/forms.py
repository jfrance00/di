import flask
import flask_wtf
import wtforms as wtf


class Location(flask_wtf.FlaskForm):
    city = wtf.SelectField('Location:', choices=['New York', 'Paris', 'Tel Aviv']) #to improve: find way to make choices
    submit = wtf.SubmitField('Submit')                                             # dynamic according to the JSON file


class CustomerItem(flask_wtf.FlaskForm):
    pass
