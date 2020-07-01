from flask import render_template,redirect,url_for,flash,request,session
from vaccine.forms import FeedbackForm,RegisterForm,LoginForm
from vaccine.models import User
from vaccine import app,db

@app.route('/feedback',methods=('GET','POST'))
#controller
def feedback():
    feedback=FeedbackForm()
    if feedback.validate_on_submit():
        session['name']=feedback.name.data
        session['email']=feedback.email.data
        session['text']=feedback.text.data
        flash("Form Submitted Successfully","success")
        return redirect(url_for('feedback'))
    #VIEW 
    return render_template('feedbackform.html',feedback=feedback)

@app.route('/register',methods=('GET','POST'))
#controller
def register():
    register=RegisterForm()
    if register.validate_on_submit():
        flash("User Created Successfully","success")
        return redirect(url_for('register'))

    return render_template('register.html',register=register)

@app.route('/login',methods=('GET','POST'))
#controller
def login():
    login=LoginForm()
    if login.validate_on_submit():
        flash("Welcome","success")
        return redirect(url_for('dashboard'))

    return render_template('login.html',login=login)


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

