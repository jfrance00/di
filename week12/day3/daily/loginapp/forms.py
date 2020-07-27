from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

class CheckName(FlaskForm):
    fname = wtf.StringField("First Name")
    lname = wtf.StringField("Last Name")
    submit = wtf.SubmitField("Enter")


class SignUp(FlaskForm):
    name = wtf.StringField("Name", valid.DataRequired())
    email = wtf.StringField("Email", valid.DataRequired())
    password = wtf.PasswordField("Password", valid.DataRequired())
    confirm_pass = wtf.PasswordField("Confirm password", valid.EqualTo(password))
    create_user = wtf.SubmitField("Sign Up")
