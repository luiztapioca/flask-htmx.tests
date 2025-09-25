from .models import User
from . import db
import random
import string


def seed_db(num_users: int = 100):
    """
    Popula a tabela User com usuários fictícios.
    Evita duplicatas caso o seeder seja rodado várias vezes.
    """

    for _ in range(num_users):
        username = "user_" + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=6)
        )

        if not User.query.filter_by(username=username).first():
            user = User(username=username)
            db.session.add(user)

    db.session.commit()
