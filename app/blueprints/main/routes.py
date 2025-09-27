from flask import Blueprint, render_template, request
from typing import Optional

from app.db.models import User
from ...db import db

main = Blueprint("main", __name__)


@main.route("/ping")
def ping():
    return "pong"


@main.get("/users")
def users():
    page: int = int(request.args.get("page", 1))
    users = User.query.paginate(page=page, per_page=10, error_out=False)

    if page > users.pages and users.pages > 0:
        page = 1
        users = User.query.paginate(page=page, per_page=10, error_out=False)

    return render_template(
        "main/index.html", users=users, page=page, num_pages=users.pages
    )
