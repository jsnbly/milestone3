from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AddUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=6, max=15)])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('passwordconfirm', message='Passwords are not the same')])
    passwordconfirm = PasswordField('Please Confirm Password')
    email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])
    submit = SubmitField('Register Account')
    