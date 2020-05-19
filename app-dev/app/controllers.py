from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User, Course, Test, Question, Result
from flask import request
from werkzeug.urls import url_parse


class UserController():

    def login():
        print('~~~~~~~ login() function called')
        form = LoginForm()
        if form.validate_on_submit():  # POST request (user clicks on Login button)
            # Check that user is in db and that password is correct
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))

            login_user(user)

            # Handling the case where a user who is not logged in requests a specific page
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                return redirect(url_for('login'))

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
            return render_template('admin.html')
        else:
            return render_template('student.html')

    def logout():
        logout_user()
        return redirect(url_for('login'))

    def register():

        form = RegistrationForm()

        if form.validate_on_submit():

            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data, email=form.email.data)

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

    def create_course():
        pass

    def edit_course():
        pass

    def delete_course():
        pass

    def rename_course():
        pass
