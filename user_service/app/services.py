from .models import User
from .auth import hash_password
from . import db


def create_user(data):
    user = User(
        username=data['username'],
        email=data['email'],
        password=hash_password(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return user
