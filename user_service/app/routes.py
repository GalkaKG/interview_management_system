from flask import Blueprint, request, jsonify
from .services import create_user
from .models import User

bp = Blueprint('users', __name__)


@bp.route("/")
def index():
    return "Hello World"


@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = create_user(data)
    return jsonify({"id": user.id, "username": user.username, "email": user.email})
