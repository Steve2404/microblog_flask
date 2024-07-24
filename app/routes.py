from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoggingForm


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Bob'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoggingForm()
    if form.validate_on_submit():
        flash(f"Login requested for {form.username.data}, remember: {form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)
