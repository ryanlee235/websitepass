from operator import ge
from flask import Blueprint, request, session, url_for, flash
from flask.templating import render_template
from sqlalchemy.sql.functions import user
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


        email_exist = User.query.filter_by(email=email).first()

        if email_exist:
            if check_password_hash(email_exist.Password, password):
                flash("Succefully logged in!", category="success")
                return redirect("/home")
            else:
                flash("email or password incorrect!",category ='error')

        else:
            flash("email does not exist!", category="error")

    return render_template("login.html")

   


    
@auth.route("/newuser", methods = ["GET", "POST"])
def new_user():
    if request.method =="POST":
        email = request.form.get("email")
        user = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")


        email_exist = User.query.filter_by(email=email).firt()
        user_exist = User.quer.filter_by(user=user).first()


        if email_exist:
            flash("email already exist!",category='error')
        elif user_exist:
            flash("username is taken!",category="error")
        elif password1 != password2:
            flash("Password does not match!",category="error")
        elif email < 6:
            flash("email not valid", category="error")
        elif password1 < 8:
            flash("password is not long enough", category="error")
        #we need to add the the information to the data base
        else:
            new_user = User(email=email, username=user, password=generate_password_hash(
                password1, method='sha256'))

    




@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.html"))




