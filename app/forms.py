from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoggingForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
