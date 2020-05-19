from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm
from app.models import User, Course, Test, Result
from flask_login import current_user, login_user, login_required, LoginManager
from app.controllers import UserController  # , CourseController


# session.permanent = True  # Allow control over session timeouts

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:  # if they're not already logged in
        return UserController.login()

    else:  # if they ARE already logged in
        return UserController.show_portal()


@app.route('/logout')
def logout():
    return UserController.logout()


@app.route('/admin')
def admin_portal():
    return render_template('admin.html', title='Admin Portal')


@app.route('/student')
def student_portal():
    return render_template('student.html', title='Student Portal')


@app.route('/admin/<course_id>')
@login_required
def course_view(course_id):
    course = Course.query.filter_by(id=course_id).first()
    tests = Test.query.filter_by(course_id=course_id)
    return render_template('admin-course.html', course=course, tests=tests)
    # return CourseController().show_tests()

# @app.route('/')

@app.route('/register', methods=['GET','POST'])
def register():
  return UserController.register()
