from enum import unique
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class user(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.string(20), nullable = False)
    email = db.Column(db.String(), nullable = False)
    password_hash = db.Column(db.String(), unique = True, nullable= False)


