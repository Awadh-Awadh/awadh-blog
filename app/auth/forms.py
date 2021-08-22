from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Length,Email,EqualTo, ValidationError
from app import db

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Enter your email',validators=[DataRequired(), Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=6),EqualTo('confirm_password', message = 'passwords must match')])
    confirm_password = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')


   




