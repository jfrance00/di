from . import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text)

    def __init__(self, todo):
        self.todo_text = todo

    def get_todos(self):
        pass

    def save_to_db(self):
        pass