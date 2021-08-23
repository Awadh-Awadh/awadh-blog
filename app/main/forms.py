from flask_wtf import FlaskForm
from  wtforms import SubmitField, StringField



class WriteForm(FlaskForm):
    title = StringField('Title')
    story = StringField('Write a story')
    submit = SubmitField('Publish')