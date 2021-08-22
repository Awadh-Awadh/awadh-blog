from enum import unique

from wtforms.fields.simple import PasswordField
from wtforms.validators import ValidationError
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class user(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.string(20), nullable = False)
    email = db.Column(db.String(), nullable = False)
    password_hash = db.Column(db.String(), unique = True, nullable= False)



    @property
    def password(self):
        raise ValidationError('Password cannot be read')


    @password.setter
    def password(self,password):
            self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        check_password_hash(self.password_hash, password)
     

    def __repr__(self):
        return '<User %r>' % self.username

