from flask import Blueprint, render_template,session
from flask_login import login_required, current_user
from .models import User, Passwords 

views = Blueprint('views',__name__)
@views.route('/')
@views.route('/home')
@login_required
def home():
    return Passwords.query.all()
    return render_template('user.html')

@login_required
#going to take the user input and create password, and also take the users website
def create_password():
    pass

@login_required
#this will just delete the password.
def delete_password():
    pass
