# flask library get Flask get 
from flask import Flask,render_template,url_for,redirect,session,flash
from math import sqrt,floor
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



class FeedbackForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    email=StringField('Email',validators=[DataRequired(),Email(message="Email format is incorrect"),
    Length(min=2,max=50,message="Name should be between 2 and 50 characters long")])
    text=StringField('Text',validators=[DataRequired()])
    passwd=PasswordField("Enter your password",validators=[DataRequired(),Length(min=6,max=50,message="Password should be between 8 and 25 characters long")])
    submit=SubmitField("Submit",validators=[DataRequired()])

app=Flask(__name__)
app.config['SECRET_KEY']='5gfg54g45tg4g5sdasdsa4g45g'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    ids=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False,unique=True)
    password=db.Column(db.String(255),nullable=False)

#create a route with name calculator
#a,b
#add,sub,mul,div
#return results in string format

@app.route('/feedback',methods=('GET','POST'))
#controller
def feedback():
    feedback=FeedbackForm()
    if feedback.validate_on_submit():
        session['name']=feedback.name.data
        session['email']=feedback.email.data
        session['text']=feedback.text.data
        flash("Form Submitted Successfully","danger")
        return redirect(url_for('feedback'))
    #VIEW 
    return render_template('feedbackform.html',feedback=feedback)

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/')
def index():
    name="farhan karim"
    user={
        'username':'fa222',
        'fname':'Farhan',
        'lname':'Karim',
    }
    return render_template('index.html',name=name,user=user)

@app.route('/maths')
def calculator():
   pass

@app.route('/maths/<float:num>')
def maths(num):
    result=sqrt(num)+floor(6.34234)
    return str(result)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % (username)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def dashboard():
    data=['$10,000','$120,000','75%','12']
    return render_template('admin/index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)