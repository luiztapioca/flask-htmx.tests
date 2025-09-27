import click
from flask.cli import with_appcontext
from .utils import seed_data, purge_data
from . import db


@click.command("init-db")
@with_appcontext
def init_db():
    """Cria as tabelas e popula o banco com seed"""
    db.create_all()  # Cria todas as tabelas
    seed_data()  # Roda o seed
    click.echo("Banco inicializado e seed rodado com sucesso!")


@click.command("purge-db")
@with_appcontext
def purge_db():
    """Cria as tabelas e popula o banco com seed"""
    purge_data()
    click.echo("Banco deletado com sucesso!")


def register_cli(app):
    app.cli.add_command(init_db)
    app.cli.add_command(purge_db)
