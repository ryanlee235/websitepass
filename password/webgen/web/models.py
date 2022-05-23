from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Passwords(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    websites = db.Column("website", db.String(100))
    user_passwords = db.Column("Password1", db.String(200))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    
    p = db.relationship("Passwords", primaryjoin="foreign(User.id) == Passwords.id")


