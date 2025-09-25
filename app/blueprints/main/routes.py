from flask import Blueprint

from app.db.models import User
from ...db import db

main = Blueprint("main", __name__)


@main.route("/ping")
def ping():
    return "pong"


@main.get("/users")
def users():
    users = User.query.all()
    return {"users": [user.username for user in users]}
