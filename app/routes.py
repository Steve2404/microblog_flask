from flask import render_template

from app import app


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Bob'}
    return render_template('index.html', title='Home', user=user)
