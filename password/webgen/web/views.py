from flask import Blueprint, render_template,session
from flask_login import login_required, current_user

views = Blueprint('views',__name__)
@views.route('/')
@views.route('/home')

def home():
    return render_template('user.html')


