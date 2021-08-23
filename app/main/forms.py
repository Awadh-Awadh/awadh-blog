from flask_wtf import FlaskForm
from  wtforms import SubmitField, StringField
from wtforms.validators import ValidationError
from ..models import User



class WriteForm(FlaskForm):
    title = StringField('Title')
    story = StringField('Write a story')
    submit = SubmitField('Publish')


class EditProfile(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    submit = SubmitField('Update')


    def username(self, field):
        user = User.query.filter_by(username = field.data).all()
        if user:
            raise ValidationError('Username exists. Please choose another username')