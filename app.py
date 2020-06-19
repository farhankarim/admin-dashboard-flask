# flask library get Flask get 
from flask import Flask,render_template,url_for
from math import sqrt,floor

app=Flask(__name__)

#create a route with name calculator
#a,b
#add,sub,mul,div
#return results in string format

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
    #declare two variables
    #perform add,sub,mul,div
    #create index.html file 
    # pass add,sub,mul,div variables to front-end
    #display them using render_template 
    
    
    return """<h1>calculator</h1>
    """+ str(num1+num2) +"""
    """+ str(num1-num2) +"""
    """+ str(num1*num2) +"""
    """+ str(num1/num2) +"""
    """

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


@app.route('/login')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)