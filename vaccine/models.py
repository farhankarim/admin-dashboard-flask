from vaccine import db

class User(db.Model):
    ids=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(255),nullable=True)
    lname=db.Column(db.String(255),nullable=True)
    age=db.Column(db.Integer,nullable=True)
    photos=db.Column(db.String(255),nullable=True)
    email=db.Column(db.String(255),nullable=True,unique=True)
    password=db.Column(db.String(255),nullable=True)

