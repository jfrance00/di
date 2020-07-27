from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(70))
    address = db.Column(db.String(100))
