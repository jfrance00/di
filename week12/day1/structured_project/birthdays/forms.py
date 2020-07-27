from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

class NewUserForm(FlaskForm):
    name = wtf.StringField("Name")
    age  = wtf.IntegerField("Age")

    submit = wtf.SubmitField("Create user")

class NewMessageForm(FlaskForm):
    name = wtf.StringField("Name", validators=[valid.DataRequired("Name can't be empty")])
    msg  = wtf.TextField("Message", validators=[valid.DataRequired("Message can't be empty")])

    submit = wtf.SubmitField("Send message")


class UserGreeting(FlaskForm):
    content = wtf.TextField("message")
    submit = wtf.SubmitField("Submit Message")