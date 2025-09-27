from . import db
import random
import string
from .models import User


def seed_data(num_users: int = 100):
    """Popula o banco com dados iniciais"""
    for _ in range(num_users):
        username = "user_" + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=6)
        )
        if not User.query.filter_by(username=username).first():
            user = User(username=username)
            db.session.add(user)
    db.session.commit()
    print("Seed concluído: usuários adicionados.")


def purge_data():
    """Limpa os dados do banco"""

    db.session.query(User).delete()
    db.session.commit()

    print("Purge concluído com sucesso: usuários removidos.")
