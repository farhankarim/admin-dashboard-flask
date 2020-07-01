from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app=Flask(__name__)
app.config['SECRET_KEY']='5gfg54g45tg4g5sdasdsa4g45g'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from vaccine import routes
