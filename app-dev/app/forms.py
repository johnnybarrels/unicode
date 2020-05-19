from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo

'''class to get hold students and admin profiles and validatos already registered'''
class LoginForm(FlaskForm):

    email          = EmailField('email', validators=[DataRequired(), Email()])
    password       = PasswordField('Password', validators=[DataRequired()])
    submit         = SubmitField('LOGIN')


''' class to hold elements and validators for the registration form '''
class RegistrationForm(FlaskForm):

    first_name     = StringField('first name', validators=[DataRequired()])
    last_name      = StringField('last name', validators=[DataRequired()])
    email          = EmailField('email', validators=[DataRequired(), Email()])
    password       = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Password again', validators=[DataRequired(), EqualTo('password')])
    submit         = SubmitField('Register')

    def validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()

        if user is not None:
            raise ValidationError('User name already taken, please use a different one')

    def validate_email(self, email):

        user = User.query.filter_by(email = username.data).first()

        if user is not None:
            raise ValidationError('Email already in use, please try a different password')


