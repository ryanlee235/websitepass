from operator import ge
from flask import Blueprint, request, session, url_for, flash
from flask.templating import render_template
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from flask_login import login_user,logout_user,login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ["GET", 'POST'])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")


        email_exist = User.query.first(email=email)
        password_exist = User.query(password= password)

        if email_exist:
            if password_exist:
                flash("Succefully logged in!", category="success")
            else:
                flash("email or password incorrect!",category ='error')

    return render_template("login.html")

   


    
@auth.route("/newuser", methods = ["GET", "POST"])
def new_user():
    pass



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.html"))
