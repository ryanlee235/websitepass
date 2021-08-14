from operator import ge
from flask import Blueprint, request, session, url_for, flash
from flask.templating import render_template
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from flask_login import login_user,logout_user,login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email)

        if user:
            if check_password_hash(user.password,password):
                flash("login successful!", category='success')
                login_user(user,remember=True)
                return redirect(url_for("home.html"))
            else:
                flash("password is incorrect", category='error')
        else:
            flash("incorrect email !", category='error')
    return render_template("login.html", user=current_user)
        


@auth.route("/newuser")
def new_user():
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get('password1')
    password2=request.form.get("password2")

    email_exist = User.query.filter_by(email=email)
    username_exist = User.query.filter_by(username=username)

    if email_exist:
        flash("email already exist! ", category="error")
    elif username_exist:
        flash("username already exist! ", category='error')
    elif password1 != password2:
        flash("password does not match!",category='error')
    elif password1 < 6:
        flash("password not long enough!", category='error')
    elif email < 4:
        flash("email is not vaild!", category="error")
    elif username < 2:
        flash("username not long enough!", category="error")

    else:
        new_user = User(emal= email, username= username, password= generate_password_hash(password1 ,method="sha256"))

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home.html"))

    return render_template("newuser.html", user = current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.html"))
