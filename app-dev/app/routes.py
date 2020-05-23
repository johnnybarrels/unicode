from flask import render_template, flash, redirect, url_for, session, jsonify
from app import app, db
from app.forms import LoginForm, NewTestForm, NewCourseForm, QuestionForm
from app.models import User, Course, Question, Test, Result
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
    course_form = NewCourseForm()
    return render_template('admin.html', title='Admin Portal', course_form=course_form)


@app.route('/student')
def student_portal():
    return render_template('student.html', title='Student Portal')


@app.route('/admin/<course_id>', methods=['GET', 'POST'])
@login_required
def course_view(course_id):
    course = Course.query.filter_by(id=course_id).first()
    tests = Test.query.filter_by(course_id=course_id)
    form = NewTestForm()
    course_form = NewCourseForm()
    return render_template('admin-course.html', course=course, tests=tests,
                           course_form=course_form, form=form)
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


@app.route('/admin/newcourse', methods=['POST'])
@login_required
def create_course():
    print('hello')
    return CourseController.create_course()


@app.route('/admin/<course_id>/<test_id>')
@login_required
def test_view(course_id, test_id):
    course_form = NewCourseForm()
    course = Course.query.filter_by(id=course_id).first()
    test = Test.query.filter_by(id=test_id).first()
    course_form = NewCourseForm()
    return render_template('admin-test-view.html', course=course,
                           course_form=course_form, test=test)


@app.route('/admin/<course_id>/<test_id>/edit')
@login_required
def edit_test(course_id, test_id):
    course = Course.query.filter_by(id=course_id).first()
    test = Test.query.filter_by(id=test_id).first()
    questions = Question.query.filter_by(test_id=test.id).all()
    form = QuestionForm()

    # if form.delete.data:
    #     return redirect(url_for('delete_question', course_id=course_id,
    #                             test_id=test_id))

    course_form = NewCourseForm()
    return render_template('admin-test-edit.html', course=course,
                           test=test, questions=questions,
                           form=form, course_form=course_form)

@app.route('/admin/<course_id>/<test_id>/deletequestion/<question_id>', methods=['GET'])
@login_required
def delete_question(course_id, test_id, question_id):
    q = Question.query.filter_by(id=question_id).first()

    db.session.delete(q)
    db.session.commit()

    return redirect(url_for('edit_test', course_id=course_id, test_id=test_id))


@app.route('/admin/<course_id>/<test_id>/newquestion', methods=['GET', 'POST'])
@login_required
def new_question(course_id, test_id):
    form = QuestionForm()

    if form.validate_on_submit():
        print('~~~~~ question form validated')
        q = Question()

        q.test_id = test_id
        q.question_type = int(form.question_type.data)
        q.question_string = form.description.data
        q.code_string = form.code_string.data
        q.mcq_1 = form.mcq_1.data
        q.mcq_2 = form.mcq_2.data
        q.mcq_3 = form.mcq_3.data
        q.mcq_4 = form.mcq_4.data
        q.answer = form.solution.data
        q.mark_alloc = form.mark_alloc.data

        db.session.add(q)
        db.session.commit()

    return redirect(url_for('edit_test', course_id=course_id, test_id=test_id))

<<<<<<< HEAD
@app.route('/add_student', methods=['GET', 'POST'])
def addStudent():
    return CourseController.addStudent()
=======


>>>>>>> 8ab38fee1b102e4660aed88aff5cb65c614740c5
