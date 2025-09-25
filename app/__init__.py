from flask import Flask


def create_app():
    app = Flask(__name__)

    from .db import init_db

    init_db(app)

    @app.cli.command("seed")
    def seeder():
        with app.app_context():
            from .db.seeder import seed_db

            seed_db()

    from app.blueprints.main.routes import main

    app.register_blueprint(main, url_prefix="/")

    return app
