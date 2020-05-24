from flask import render_template, flash, redirect, url_for, session, jsonify
from app import app, db
from app.forms import LoginForm, NewTestForm, NewCourseForm, QuestionForm, RenameTestForm, QuestionSubmissionForm
from app.models import User, Course, Question, Test, Submission, Result
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
    course = Course.query.filter_by(id=course_id).first()
    test = Test.query.filter_by(id=test_id).first()
    course_form = NewCourseForm()
    results = Result.query.filter_by(test_id=test.id).all()
    rename_test_form = RenameTestForm()

    return render_template('admin-test-view.html', course=course,
                           course_form=course_form, test=test,
                           rename_test_form=rename_test_form,
                           results=results)


@app.route('/admin/<course_id>/<test_id>/edit', methods=['GET'])
@login_required
def edit_test(course_id, test_id):
    course = Course.query.filter_by(id=course_id).first()
    test = Test.query.filter_by(id=test_id).first()
    questions = Question.query.filter_by(test_id=test.id).all()
    form = QuestionForm()

    course_form = NewCourseForm()
    return render_template('admin-test-edit.html', course=course,
                           test=test, questions=questions,
                           form=form, course_form=course_form)


@app.route('/admin/<course_id>/<test_id>/rename', methods=['POST'])
@login_required
def rename_test(course_id, test_id):
    test = Test.query.filter_by(id=test_id).first()
    form = RenameTestForm()

    if form.validate_on_submit():
        test.name = form.new_test_name.data
        db.session.commit()

        redirect(url_for('test_view', course_id=course_id, test_id=test_id))

    return redirect(url_for('test_view', course_id=course_id, test_id=test_id))


@app.route('/admin/<course_id>/<test_id>/makelive', methods=['POST'])
@login_required
def toggle_live(course_id, test_id):
    test = Test.query.filter_by(id=test_id).first()
    if test.is_live:
        test.is_live = False
    else:
        test.is_live = True
    db.session.commit()

    return redirect(url_for('course_view', course_id=course_id))


@app.route('/admin/<course_id>/<test_id>/edit_question/<question_id>', methods=['POST'])
@login_required
def edit_question(course_id, test_id, question_id):
    course = Course.query.filter_by(id=course_id).first()
    test = Test.query.filter_by(id=test_id).first()
    q = Question.query.filter_by(id=question_id).first()
    form = QuestionForm()

    if form.delete.data:
        db.session.delete(q)
        db.session.commit()

        return redirect(url_for('edit_test', course_id=course_id,
                                test_id=test_id))

    if form.validate_on_submit():
        if form.save.data:
            q.test_id = test_id
            q.question_type = int(form.question_type.data)
            q.question_string = repr(form.description.data.encode())[2:-1]
            q.code_string = repr(form.code_string.data.encode())[2:-1]
            q.mcq_1 = form.mcq_1.data
            q.mcq_2 = form.mcq_2.data
            q.mcq_3 = form.mcq_3.data
            q.mcq_4 = form.mcq_4.data
            q.mcq_answer = form.mcq_solution.data
            q.answer = form.solution.data
            q.mark_alloc = form.mark_alloc.data
            db.session.commit()

            return redirect(url_for('edit_test', course_id=course_id,
                                    test_id=test_id))


@app.route('/admin/<course_id>/<test_id>/deletequestion/<question_id>', methods=['POST'])
@login_required
def delete_question(course_id, test_id, question_id):
    q = Question.query.filter_by(id=question_id).first()

    db.session.delete(q)
    db.session.commit()

    return redirect(url_for('edit_test', course_id=course_id, test_id=test_id))


@app.route('/admin/<course_id>/<test_id>/newquestion', methods=['POST'])
@login_required
def new_question(course_id, test_id):
    form = QuestionForm()

    if form.validate_on_submit():
        q = Question()
        q.test_id = test_id
        q.question_type = int(form.question_type.data)
        q.question_string = repr(form.description.data.encode())[2:-1]
        q.code_string = repr(form.code_string.data.encode())[2:-1]
        q.mcq_1 = form.mcq_1.data
        q.mcq_2 = form.mcq_2.data
        q.mcq_3 = form.mcq_3.data
        q.mcq_4 = form.mcq_4.data
        q.mcq_answer = form.mcq_solution.data
        q.answer = form.solution.data
        q.mark_alloc = form.mark_alloc.data

        db.session.add(q)
        db.session.commit()

    # for field, error in form.errors.items():
    #     print(f'~~~~~~~~ {field}: {error}')
    return redirect(url_for('edit_test', course_id=course_id, test_id=test_id))


@app.route('/student/<course_id>/<test_id>/taketest')
@login_required
def take_test(course_id, test_id):
    course = Course.query.filter_by(id=course_id).first()
    test = Test.query.filter_by(id=test_id).first()
    questions = Question.query.filter_by(test_id=test.id).all()
    form = QuestionSubmissionForm()

    return render_template('take-test.html', course=course, test=test,
                           questions=questions, form=form)


@app.route('/student/<course_id>/<test_id>/<question_id>/submit', methods=['POST'])
@login_required
def new_submission(course_id, test_id, question_id):
    q = Question.query.filter_by(id=question_id).first()
    sub = Submission.query.filter_by(question_id=question_id).first()
    if not sub:  # if no existing submission exists
        sub = Submission()
        sub.user_id = current_user.id
        sub.question_id = question_id

    # mcq_options = q.get_mcq_options()

    form = QuestionSubmissionForm()

    if form.validate_on_submit():
        print('~~~~~~~~ submission form validated')
        if q.question_type == 1:
            sub.output_sub = form.output_answer.data
        elif q.question_type == 2:
            sub.mcq_sub = form.mcq_answer.data
        elif q.question_type == 3:
            sub.code_sub = repr(form.code_answer.data)[1:-1]

        db.session.add(sub)
        db.session.commit()

    return redirect(url_for('take_test', course_id=course_id, test_id=test_id))
