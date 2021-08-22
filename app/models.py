from enum import unique
from sqlalchemy.orm import backref

from wtforms.fields.simple import PasswordField
from wtforms.validators import ValidationError
from . import db
#from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.string(20), nullable = False)
    email = db.Column(db.String(), nullable = False)
    posts = db.relationship('Posts', backref = 'author', lazy = 'dynamic')


class Posts (db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.string(20), nullable = False)
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))




    # @property
    # def password(self):
    #     raise ValidationError('Password cannot be read')


    # @password.setter
    # def password(self,password):
    #         self.password_hash = generate_password_hash(password)


    # def verify_password(self,password):
    #     check_password_hash(self.password_hash, password)
     

    def __repr__(self):
        return '<User %r>' % self.username

