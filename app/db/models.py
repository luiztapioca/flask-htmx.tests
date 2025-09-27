from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)

    def __init__(self, username: str):
        self.username = username

    def __repr__(self):
        return f"<User {self.username}>"
