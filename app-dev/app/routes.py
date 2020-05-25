from flask import render_template, flash, redirect, url_for, session, jsonify
from app import app, db
from app.forms import LoginForm, NewTestForm, NewCourseForm, QuestionForm, RenameTestForm, QuestionSubmissionForm
from app.models import User, Course, Question, Test, Submission, Result
from flask_login import current_user, login_user, login_required, LoginManager
from app.controllers import UserController, CourseController, TestController


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
    if not current_user.is_admin:
        return redirect(url_for('student_portal'))
    course_form = NewCourseForm()
    return render_template('admin.html', title='Admin Portal', course_form=course_form)


@app.route('/student')
def student_portal():
    return render_template('student.html', title='Student Portal')


@app.route('/course_view/<course_id>', methods=['GET'])
@login_required
def course_view(course_id):
    return UserController.course_view(course_id)

    # return CourseController().show_tests()


@app.route('/course_view/<course_id>/addstudent', methods=['POST'])
@login_required
def add_student_course(course_id):
    return CourseController.add_student(course_id)


@app.route('/course_view/<course_id>/removestudent/<student_id>', methods=['POST'])
def remove_student_course(course_id, student_id):
    return CourseController.remove_student(course_id, student_id)


@app.route('/admin/<course_id>/createtest', methods=['POST'])
@login_required
def create_test(course_id):
    return CourseController.create_test(course_id)


@app.route('/admin/newcourse', methods=['POST'])
@login_required
def create_course():
    print('hello')
    return CourseController.create_course()


@app.route('/admin/<course_id>/deletetest/<test_id>', methods=['GET'])
@login_required
def delete_test(course_id, test_id):
    return TestController.delete_test(course_id, test_id)


@app.route('/admin/<course_id>/<test_id>')
@login_required
def test_view(course_id, test_id):
    return TestController.show_test(course_id, test_id)


@app.route('/admin/<course_id>/<test_id>/edit', methods=['GET'])
@login_required
def edit_test_view(course_id, test_id):
    return TestController.edit_test_view(course_id, test_id)


@app.route('/admin/<course_id>/<test_id>/rename', methods=['POST'])
@login_required
def rename_test(course_id, test_id):
    return TestController.rename_test(course_id, test_id)


@app.route('/admin/<course_id>/<test_id>/makelive', methods=['POST'])
@login_required
def toggle_live(course_id, test_id):
    return TestController.toggle_live(course_id, test_id)


@app.route('/admin/<course_id>/<test_id>/edit_question/<question_id>', methods=['POST'])
@login_required
def edit_question(course_id, test_id, question_id):
    return TestController.edit_question(course_id, test_id, question_id)


@app.route('/admin/<course_id>/<test_id>/deletequestion/<question_id>', methods=['POST'])
@login_required
def delete_question(course_id, test_id, question_id):
    return TestController.delete_question(course_id, test_id, question_id)


@app.route('/admin/<course_id>/<test_id>/newquestion', methods=['POST'])
@login_required
def new_question(course_id, test_id):
    return TestController.new_question(course_id, test_id)


@app.route('/student/<course_id>/<test_id>/taketest')
@login_required
def take_test(course_id, test_id):
    return TestController.take_test(course_id, test_id)


@app.route('/student/<course_id>/<test_id>/test')
@login_required
def student_test_view(course_id, test_id):
    return TestController.show_test(course_id, test_id)

# @app.route('/student/<course_id>/<test_id>/<question_id>/submit_test', methods=['POST'])
# @login_required
# def submit_test(course_id, test_id):
#     return TestController.submit_test(course_id, test_id)


@app.route('/student/<course_id>/<test_id>/<question_id>/submit', methods=['POST'])
@login_required
def new_submission(course_id, test_id, question_id):
    return TestController.new_submission(course_id, test_id, question_id)


@app.route('/student/<course_id>/<test_id>/submit', methods=['POST'])
@login_required
def submit_test(course_id, test_id):
    return TestController.submit_test(course_id, test_id)


@app.route('/admin/<course_id>/<test_id>/<student_id>')
@login_required
def mark_test(course_id, test_id, student_id):
    return TestController.mark_test(course_id, test_id, student_id)


@app.route('/admin/<course_id>/<test_id>/<student_id>/<submission_id>', methods=['POST'])
@login_required
def mark_submission(course_id, test_id, student_id, submission_id):
    return TestController.mark_submission(course_id, test_id, student_id, submission_id)


@app.route('/admin/<course_id>/<test_id>/<student_id>/submit', methods=['POST'])
@login_required
def submit_and_feedback(course_id, test_id, student_id):
    return TestController.submit_and_feedback(course_id, test_id, student_id)


@app.route('/aggregateview', methods=['GET'])
def aggregate_view():
    return CourseController.aggregate_view()
