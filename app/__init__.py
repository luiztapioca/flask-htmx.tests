from flask import Flask
from . import db
from .db.cli import register_cli


def create_app():
    app = Flask(__name__)

    db.init_db(app)
    register_cli(app)

    from app.blueprints.main.routes import main

    app.register_blueprint(main, url_prefix="/")

    app.debug = True

    return app
