import wtforms as wtf
from flask_wtf import FlaskForm


class SearchInput(FlaskForm):
    name = wtf.StringField("Name")
    number = wtf.StringField("Number")
    submit = wtf.SubmitField("Search")


class AddToDatabase(FlaskForm):
    id = wtf.IntegerField('id')
    name =wtf.StringField("Name")
    email = wtf.StringField('Email')
    phone = wtf.StringField("Phone")
    address = wtf.StringField("Address")
    submit = wtf.SubmitField("Add")


