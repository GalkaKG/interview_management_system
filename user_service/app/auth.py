import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import current_app


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.now(datetime.UTC) + timedelta(hours=1)
    }

    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

