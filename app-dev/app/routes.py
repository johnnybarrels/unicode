from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        flash(
            f'Login requested for user {form.email.data}')
        return redirect('/index')

    return render_template('index.html', form=form)


@app.route('/admin')
def admin_portal():

    return render_template('admin.html')
