from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import db

    db.init_db(app)

    @app.cli.command("seed")
    def seeder():
        with app.app_context():
            from .db import seeder

            seeder.seed_db()

    from app.blueprints.main.routes import main

    app.register_blueprint(main, url_prefix="/")

    return app
