from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo


class LoginForm(FlaskForm):

    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('LOGIN')


class RegistrationForm(FlaskForm):

    first_name = StringField('first name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Password', validators=[
                                   DataRequired(), EqualTo('password')])
    submit = SubmitField('REGISTER')


class NewCourseForm(FlaskForm):

    course_name = StringField('Course Name', validators=[DataRequired()])
    course_code = StringField('Course Code', validators=[DataRequired()])
    submit = SubmitField('Create Course')

class NewTestForm(FlaskForm):
    test_name = StringField('Test Name', validators=[DataRequired()])
    submit = SubmitField('Create Test')
