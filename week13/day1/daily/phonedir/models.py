from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(13))
    email = db.Column(db.String(25))
    address = db.Column(db.String(80))