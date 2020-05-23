from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, NewTestForm, NewCourseForm
from app.models import User, Course, Test, Question, Result
from flask import request
from werkzeug.urls import url_parse


class UserController():

    def login():
        
        form = LoginForm()
        if form.validate_on_submit():  # POST request (user clicks on Login button)
            # Check that user is in db and that password is correct
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))

            login_user(user)

            # Handling the case where a user who is not logged in requests a specific page
            # next_page = request.args.get('next')
            # if not next_page or url_parse(next_page).netloc != '':
            #     return redirect(url_for('login'))

            # return redirect(next_page)

            if user.is_admin:
                return redirect(url_for('admin_portal'))
            else:
                # return render_template('student.html')
                return redirect(url_for('student_portal'))

        # for GET request (browser loading page)
        return render_template('index.html', form=form)

    def show_portal():
        if current_user.is_admin:
            course_form = NewCourseForm()
            return render_template('admin.html', course_form=course_form)
        else:
            return render_template('student.html')

    def logout():
        logout_user()
        return redirect(url_for('login'))

    def register():

        form = RegistrationForm()

        if form.validate_on_submit():

            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data, email=form.email.data,
                        is_admin=1)

            # If submitted email is already in db
            if User.query.filter_by(email=user.email).first() is not None:

                flash('Email is already registered')
                return redirect(url_for('register'))

            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()

            flash("You have registered")

            return redirect(url_for('login'))

        return render_template('register.html', title="Register", form=form)

    

class CourseController():

    def get_tests():
        tests = Test.query.filter_by()

    def create_test(course_id):
        form = NewTestForm()
        course = Course.query.filter_by(id=course_id).first()
        tests = Test.query.filter_by(course_id=course_id)
        if form.validate_on_submit():
            test = Test()
            test.name = form.test_name.data
            test.course_id = course.id

            db.session.add(test)
            db.session.commit()

            return redirect(url_for('course_view', course_id=course.id))

        # TODO: proper input validation - diff return values? flash something? done on frontend?
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
        
    def edit_course():
        pass

    def delete_course():
        pass

    def rename_course():
        pass


"""
class TestController():

    def create_test():
        form = NewTestForm()
        pass
"""
