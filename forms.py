from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SubmitField, SelectField 
from wtforms.validators import DataRequired,Length,Email,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class AddUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=6, max=15)])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('passwordconfirm', message='Passwords are not the same')])
    passwordconfirm = PasswordField('Confirm Password')
    email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])
    submit = SubmitField('Register Account')

class AddRecipe(FlaskForm):
    title = StringField('Recipe Title', validators=[DataRequired()])
    tags = StringField('Tags to Describe the Recipe', validators=[DataRequired()])
    preptime = StringField('Cooking Time', validators=[DataRequired()])
    image = StringField('Link to Recipe Image', validators=[DataRequired()])
    discription = TextAreaField('Description of Recipe', validators=[DataRequired()])
    ingredient = TextAreaField('Ingredients Required', validators=[DataRequired()])
    instructions = TextAreaField('Recipe Instructions', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')

class EditRecipe(FlaskForm):
    title = StringField('Recipe Title', validators=[DataRequired()])
    tags = StringField('Tags to Describe the Recipe', validators=[DataRequired()])
    preptime = StringField('Cooking Time', validators=[DataRequired()])
    image = StringField('Link to Recipe Image', validators=[DataRequired()])
    discription = TextAreaField('Description of Recipe', validators=[DataRequired()])
    ingredient = TextAreaField('Ingredients Required', validators=[DataRequired()])
    instructions = TextAreaField('Recipe Instructions', validators=[DataRequired()])
    submit = SubmitField('Edit Recipe')
    