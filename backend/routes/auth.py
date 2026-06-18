from flask import Blueprint, request

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models.db import db
from models.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return {
            "error": "name, email and password are required"
        }, 400

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return {
            "error": "Email already registered"
        }, 409

    password_hash = generate_password_hash(
        password
    )

    user = User(
        name=name,
        email=email,
        password_hash=password_hash
    )

    db.session.add(user)
    db.session.commit()

    return {
        "message": "User registered successfully"
    }, 201


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {
            "error": "email and password are required"
        }, 400

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return {
            "error": "Invalid email or password"
        }, 401

    if not check_password_hash(
        user.password_hash,
        password
    ):
        return {
            "error": "Invalid email or password"
        }, 401

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }, 200