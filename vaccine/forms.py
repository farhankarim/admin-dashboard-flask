from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms.fields.html5 import EmailField

class FeedbackForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    email=StringField('Email',validators=[DataRequired(),Email(message="Email format is incorrect"),
    Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    text=StringField('Text',validators=[DataRequired()])
    passwd=PasswordField("Enter your password",validators=[DataRequired(),Length(min=6,max=50,message="Password should be between 8 and 25 characters long")])
    submit=SubmitField("Submit",validators=[DataRequired()])

class RegisterForm(FlaskForm):
    fname=StringField(' First Name',validators=[DataRequired(),Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    lname=StringField(' Last Name',validators=[DataRequired(),Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    email=EmailField(' Email',validators=[DataRequired(),Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    passwd=PasswordField("Enter your password",validators=[DataRequired(),Length(min=6,max=50,message="Password should be between 8 and 25 characters long"),EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit=SubmitField("Submit",validators=[DataRequired()])

class LoginForm(FlaskForm):
    email=EmailField(' Email',validators=[DataRequired(),Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    passwd=PasswordField("Enter your password",validators=[DataRequired(),Length(min=6,max=50,message="Password should be between 8 and 25 characters long")])
    submit=SubmitField("Submit",validators=[DataRequired()])
    