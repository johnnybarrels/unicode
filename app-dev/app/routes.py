from flask import render_template, flash, redirect, url_for, session, jsonify
from app import app, db
from app.forms import LoginForm, NewTestForm, NewCourseForm
from app.models import User, Course, Test, Result
from flask_login import current_user, login_user, login_required, LoginManager
from app.controllers import UserController, CourseController

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    return UserController.register()


@app.route('/admin')
def admin_portal():
    return render_template('admin.html', title='Admin Portal')


@app.route('/student')
def student_portal():
    return render_template('student.html', title='Student Portal')


@app.route('/admin/<course_id>', methods=['GET', 'POST'])
@login_required
def course_view(course_id):
    course = Course.query.filter_by(id=course_id).first()
    tests = Test.query.filter_by(course_id=course_id)
    form = NewTestForm()
    return render_template('admin-course.html', course=course, tests=tests, form=form)
    # return CourseController().show_tests()


"""
@app.route('/admin/createcourse', methods=['GET', 'POST'])
@login_required
def create_course():

    form = NewCourseForm()
    
    if form.validate_on_submit():
        course = Course()
        course.name = form.course_name.data
        course.course_code = form.course_code.data
        
        db.session.add()
        db.session.commit()
    
        return redirect(url_for('admin_portal'))
    return redirect(url_for('admin_portal'))
"""


@app.route('/admin/<course_id>/createtest', methods=['POST'])
@login_required
def create_test(course_id):
    return CourseController.create_test(course_id)


@app.route('/admin/<course_id>/deletetest/<test_id>', methods=['GET'])
@login_required
def delete_test(course_id, test_id):
    test = Test.query.filter_by(id=test_id).first()

    db.session.delete(test)
    db.session.commit()

    return redirect(url_for('course_view', course_id=course_id))


@app.route('/admin/newcourse')
@login_required
def create_course():
    return CourseController.create_course()


@app.route('/admin/<course_id>/<test_id>')
@login_required
def test_view(course_id, test_id):
    # test = Test.query.filter_by(id=test_id).first()
    return render_template('admin-test-view.html')


@app.route('/admin/<course_id>/<test_id>/edit')
def edit_test(course_id, test_id):
    return render_template('admin-test-edit.html')
