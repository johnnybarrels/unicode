from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm
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

            if user.is_admin:
                return redirect(url_for('admin_portal'))
            else:
                # return render_template('student.html')
                return redirect(url_for('student_portal'))
        
        else:  # for GET request (browser loading page)
            return render_template('index.html', form=form)

    def show_portal():
        if current_user.is_admin:
            return render_template('admin.html')
        else:
            return render_template('student.html')

    def logout():
        logout_user()
        return redirect(url_for('login'))



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







