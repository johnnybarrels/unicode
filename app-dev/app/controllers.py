from app import app, db
from flask import request
from app.models import User, Course, Test, Question, Result, enrolments, Submission
from app.forms import LoginForm, RegistrationForm, NewTestForm, NewCourseForm, RenameTestForm, QuestionForm, QuestionSubmissionForm, AddStudentToCourseForm, MarkTestForm, FeedbackForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required


class UserController():

    def login():

        form = LoginForm()
        if form.validate_on_submit():
            # Check that user is in db and that password is correct
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))

            login_user(user)

            if user.is_admin:
                return redirect(url_for('admin_portal'))
            else:
                return redirect(url_for('student_portal'))

        # for GET request (browser loading page)
        return render_template('index.html', form=form)

    def show_portal():
        if current_user.is_admin:
            course_form = NewCourseForm()
            return render_template('admin.html', course_form=course_form)
        else:
            return render_template('student.html')

    def course_view(course_id):
        course = Course.query.filter_by(id=course_id).first()
        tests = course.tests

        form = NewTestForm()
        rename_test_form = RenameTestForm()
        course_users = course.get_users()

        new_test_form = NewTestForm()
        course_form = NewCourseForm()
        add_student_form = AddStudentToCourseForm()

        if current_user.is_admin:
            return render_template('admin-course.html', add_student_form=add_student_form,
                                   rename_test_form=rename_test_form, course_users=course_users,
                                   course_form=course_form, new_test_form=new_test_form, course=course,
                                   tests=tests)

        else:
            live_tests = [test for test in tests if test.is_live]
            return render_template('student-course.html', course=course, tests=live_tests)

    def logout():
        logout_user()
        return redirect(url_for('login'))

    def register():

        form = RegistrationForm()

        if form.validate_on_submit():

            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data, email=form.email.data,
                        is_admin=0)

            # If submitted email is already in db
            if User.query.filter_by(email=user.email).first() is not None:

                flash('Email is already registered!')
                flash('Please log in below')
                return redirect(url_for('login'))

            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()

            flash("You have registered")
            flash("Please log in below")

            return redirect(url_for('login'))

        return render_template('register.html', title="Register", form=form)


class CourseController():

    def aggregate_view():
        courses = Course.query.all()
        return render_template('general-dashboard.html', courses=courses)

    def create_test(course_id):
        form = NewTestForm()
        course = Course.query.filter_by(id=course_id).first()
        tests = course.tests
        if form.validate_on_submit():
            test = Test()
            test.name = form.test_name.data
            test.course_id = course.id

            db.session.add(test)
            db.session.commit()

            return redirect(url_for('course_view', course_id=course.id))

        return redirect(url_for('course_view', course_id=course.id))

    def create_course():
        course_form = NewCourseForm()

        if course_form.validate_on_submit():
            course = Course()
            course.name = course_form.course_name.data
            course.course_code = course_form.course_code.data

            db.session.add(course)
            current_user.courses.append(course)
            db.session.commit()

            return redirect(url_for('admin_portal'))

        return redirect(url_for('admin_portal', course_form=course_form))

    def add_student(course_id):
        add_student_form = AddStudentToCourseForm()
        course = Course.query.filter_by(id=course_id).first()
        if add_student_form.validate_on_submit():
            student_email = add_student_form.student_email.data
            student = User.query.filter_by(email=student_email).first()
            if student:
                student.courses.append(course)
                db.session.commit()

            return redirect(url_for('course_view', course_id=course_id))

        return redirect(url_for('course_view', course_id=course_id))

    def remove_student(course_id, student_id):
        course = Course.query.filter_by(id=course_id).first()
        student = User.query.filter_by(id=student_id).first()

        if student:
            student.courses.remove(course)
            db.session.commit()

            return redirect(url_for('course_view', course_id=course_id))

        return redirect(url_for('course_view', course_id=course_id))


class TestController():

    def create_test():
        form = NewTestForm()
        pass

    def delete_test(course_id, test_id):
        test = Test.query.filter_by(id=test_id).first()

        db.session.delete(test)
        db.session.commit()

        return redirect(url_for('course_view', course_id=course_id))

    def show_test(course_id, test_id):
        course = Course.query.filter_by(id=course_id).first()
        test = Test.query.filter_by(id=test_id).first()
        users = course.get_users()

        max_mark = test.get_max_mark()
        min_mark = test.get_min_mark()
        test_avg = test.get_average_mark()

        if current_user.is_admin:
            num_results = test.get_num_results()
            num_enrolled_students = course.get_num_enrolments()

            aggregates = [num_results, num_enrolled_students,
                          test_avg, max_mark, min_mark]

            submitted_users = test.get_submitted_users()

            rename_test_form = RenameTestForm()
            course_form = NewCourseForm()

            return render_template('admin-test-view.html', course=course,
                                   course_form=course_form, test=test,
                                   rename_test_form=rename_test_form,
                                   submitted_users=submitted_users, aggregates=aggregates)   # results=results
        else:
            student_result = test.get_student_result(current_user.id)
            aggregates = []
            if student_result:
                student_perc = round(student_result.score / test.total_marks() * 100, 2)
                aggregates = [student_perc,
                              test_avg, max_mark, min_mark]

            return render_template('student-test-view.html',
                                   aggregates=aggregates,
                                   test=test, course=course,
                                   student_result=student_result)

    def edit_test_view(course_id, test_id):

        course = Course.query.filter_by(id=course_id).first()
        test = Test.query.filter_by(id=test_id).first()
        questions = test.questions

        form = QuestionForm()
        course_form = NewCourseForm()

        return render_template('admin-test-edit.html', course=course,
                               test=test, questions=questions,
                               form=form, course_form=course_form)

    def rename_test(course_id, test_id):
        test = Test.query.filter_by(id=test_id).first()
        form = RenameTestForm()

        if form.validate_on_submit():
            test.name = form.new_test_name.data
            db.session.commit()

            redirect(url_for('test_view', course_id=course_id, test_id=test_id))

        return redirect(url_for('test_view', course_id=course_id, test_id=test_id))

    def toggle_live(course_id, test_id):
        test = Test.query.filter_by(id=test_id).first()

        if test.is_live:
            test.is_live = False
        else:
            test.is_live = True

        db.session.commit()

        return redirect(url_for('course_view', course_id=course_id))

    def edit_question(course_id, test_id, question_id):
        course = Course.query.filter_by(id=course_id).first()
        test = Test.query.filter_by(id=test_id).first()
        q = Question.query.filter_by(id=question_id).first()
        form = QuestionForm()

        if form.delete.data:
            db.session.delete(q)
            db.session.commit()

            return redirect(url_for('edit_test_view', course_id=course_id,
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

                return redirect(url_for('edit_test_view', course_id=course_id,
                                        test_id=test_id))

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

        return redirect(url_for('edit_test_view', course_id=course_id, test_id=test_id))

    def take_test(course_id, test_id):
        course = Course.query.filter_by(id=course_id).first()
        test = Test.query.filter_by(id=test_id).first()
        questions = test.questions

        form = QuestionSubmissionForm()

        return render_template('take-test.html', course=course, test=test, questions=questions, form=form)

    def new_submission(course_id, test_id, question_id):
        q = Question.query.filter_by(id=question_id).first()
        sub = q.get_user_submission(current_user.id)
        if not sub:  # if no existing submission exists
            sub = Submission()
            sub.user_id = current_user.id
            sub.test_id = test_id
            sub.question_id = question_id

        form = QuestionSubmissionForm()
        if form.validate_on_submit():
            if q.question_type == 1:
                sub.output_sub = form.output_answer.data
            elif q.question_type == 2:
                sub.mcq_sub = form.mcq_answer.data
            elif q.question_type == 3:
                sub.code_sub = repr(form.code_answer.data)[1:-1]

            db.session.add(sub)
            db.session.commit()

        return redirect(url_for('take_test', course_id=course_id, test_id=test_id))

    def submit_test(course_id, test_id):
        test = Test.query.filter_by(id=test_id).first()
        user_id = current_user.id
        questions = test.questions  # Question.query.filter_by(test_id=test_id)
        submissions = test.get_user_submissions(user_id)

        total = 0
        for submission in submissions:
            submission.auto_mark()
            total += submission.score

        result = Result(user_id=user_id, test_id=test_id, score=total)
        db.session.add(result)
        db.session.commit()

        if not any([q.question_type == 3 for q in questions]):
            result.needs_marking = False

        return redirect(url_for('course_view', course_id=course_id))

    def mark_test(course_id, test_id, student_id):
        course = Course.query.filter_by(id=course_id).first()
        test = Test.query.filter_by(id=test_id).first()
        questions = test.questions
        student = User.query.filter_by(id=student_id).first()

        submissions = test.get_user_submissions(student_id)

        course_form = NewCourseForm()
        feedback_form = FeedbackForm()

        form = MarkTestForm()

        return render_template('mark-test.html', course=course,
                               course_form=course_form, student=student,
                               test=test, questions=questions,
                               submissions=submissions, form=form,
                               feedback_form=feedback_form)

    def mark_submission(course_id, test_id, student_id, submission_id):
        submission = Submission.query.filter_by(id=submission_id).first()
        result = Result.query.filter_by(
            test_id=test_id, user_id=student_id).first()

        form = MarkTestForm()

        form = MarkTestForm()

        if form.validate_on_submit():
            score_diff = form.mark.data - submission.score
            submission.score = form.mark.data
            submission.needs_marking = False

            # incrementally storing scores in case a teacher
            # doesn't finish marking a student's test
            result.score += score_diff

            db.session.commit()

        return redirect(url_for('mark_test', course_id=course_id, test_id=test_id,
                                student_id=student_id))

    def submit_and_feedback(course_id, test_id, student_id):
        test = Test.query.filter_by(id=test_id).first()
        result = Result.query.filter_by(
            test_id=test_id, user_id=student_id).first()
        submissions = test.get_user_submissions(student_id)

        form = FeedbackForm()
        if form.validate_on_submit():
            result.feedback = form.feedback.data
            result.score = sum((sub.score for sub in submissions))
            if not any(sub.needs_marking for sub in submissions):
                result.needs_marking = False

            db.session.commit()

        return redirect(url_for('test_view', course_id=course_id, test_id=test_id))
