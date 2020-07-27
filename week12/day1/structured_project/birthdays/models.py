from . import db

# First - Create a class that inherit from db.Model
class User(db.Model):

    id   = db.Column(db.Integer, primary_key=True)

    # Second - Create your model's columns
    name = db.Column(db.String(64))
    age  = db.Column(db.Integer)


class GreetingMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
