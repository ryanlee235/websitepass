from . import db
from sqlalchemy.sql import func

class User(db.Model):
    #every single row needs to have a different id, primary key makes sure there is only one kind of data
    _id = db.Columm("id",db.Integer, primary_key=True)
    email = db.Column("email", db.String(100))
    user_name= db.Column("user",db.String(100))
    password = db.Column("password",db.String(100))



class Passwords(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    website = db.Column("website", db.String(100))
    password = db.Column("Password1", db.string(200))

