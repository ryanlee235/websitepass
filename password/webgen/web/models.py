from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    


class Passwords(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    website = db.Column("website", db.String(100))
    user_passwords = db.Column("Password1", db.String(200))

    

