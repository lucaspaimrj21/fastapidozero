from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='lucas',
        email='lucas@paim.com.br',
        password='minha_senha_boladona',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'lucas@paim.com.br')
    )

    assert result.id == 1
