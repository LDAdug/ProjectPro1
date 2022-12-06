from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired
from app.models import User

from wtforms.validators import Length
from wtforms import TextAreaField



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Preferred Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PostForm(FlaskForm):
    post = TextAreaField("What's on your mind. ", validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Post')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class Search(FlaskForm):
    username = StringField("Search for Username",validators=[DataRequired()])
    submit = SubmitField("Submit")

class MessageForm(FlaskForm):
    message = TextAreaField("Send a private message", validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')