from flask import Flask


def create_app():
    app = Flask(__name__)

    from .db import init_db

    init_db(app)

    from app.blueprints.main.routes import main

    app.register_blueprint(main, url_prefix="/")

    return app
