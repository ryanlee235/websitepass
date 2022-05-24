from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Passwords(db.Model):
    __tablename__ ="password"
    id = db.Column("id", db.Integer, primary_key=True)
    websites = db.Column("website", db.String(100))
    user_passwords = db.Column("Password1", db.String(200))
    password_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    passwords = db.relationship("Passwords", backref="password")
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    
    

