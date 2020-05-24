from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from wtforms.fields.html5 import EmailField
from wtforms.widgets import HTMLString
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, HiddenField, RadioField, Field, SelectField


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


class RenameTestForm(FlaskForm):
    new_test_name = StringField('New Test Name', validators=[DataRequired()])
    submit = SubmitField('Save')


class QuestionForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    code_string = TextAreaField('Code')
    solution = StringField('Solution')
    mcq_1 = StringField('MCQ Option 1')
    mcq_2 = StringField('MCQ Option 2')
    mcq_3 = StringField('MCQ Option 3')
    mcq_4 = StringField('MCQ Option 4')
    mcq_solution = RadioField('MCQ Solution', choices=[(
        let, let) for let in 'abcd'], validate_choice=False)
    mark_alloc = IntegerField('Allocated mark', validators=[DataRequired()])
    question_type = HiddenField(
        'Question Type', default=1, validators=[DataRequired()])
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class AddStudentToCourseForm(FlaskForm):
    student_email = StringField('Student Email', validators=[DataRequired()])
    submit = SubmitField('Add Student')


class QuestionSubmissionForm(FlaskForm):
    description = TextAreaField('Question Description')
    output_answer = StringField('Output Question Answer')
    mcq_answer = HiddenField('MCQ Answer')
    code_answer = TextAreaField('Code Answer')
    submit = SubmitField('Submit')
