from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    #every single row needs to have a different id, primary key makes sure there is only one kind of data
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column( db.String(100), unique =True)
    username= db.Column(db.String(100), unique =True)
    Passwords = db.Column(db.String(100))
    



class Passwords(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    website = db.Column("website", db.String(100))
    password = db.Column("Password1", db.String(200))

    

