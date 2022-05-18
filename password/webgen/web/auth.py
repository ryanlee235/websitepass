from flask import Blueprint, request, session, url_for, flash
from flask.templating import render_template
from sqlalchemy.sql.functions import user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from flask_login import login_user,logout_user,login_required, current_user
#setting up blueprint
auth = Blueprint('auth', __name__)
#making a url with http methods.
@auth.route("/login", methods = ["GET", 'POST'])
def login():
    # if the website is sending information
    if request.method == "POST":
        #grabe the email from the website
        email = request.form.get("email")
        #grab the password from the website
        password = request.form.get("password")

        # we are looking in the database under the column email, and grabbing the first one 
        user = User.query.filter_by(email=email).first()

        if user:
            #checking the password with the hash method
            if check_password_hash(user.Passwords, password):
                #tell the user they have been logged in 
                flash("Succefully logged in!", category="success")
                login_user(user,remember=True)
                #gets redirected to the home page/ user page
                return redirect("/home")
            else:
                flash("email or password incorrect!",category ='error')

        else:
            flash("email does not exist!", category="error")

    return render_template("login.html",user =current_user)

   
@auth.route("/newuser", methods = ["GET", "POST"])
def new_user():
    if request.method =="POST":
        email = request.form.get("email")
        user = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")


        email_exist = User.query.filter_by(email=email).first()
        user_exist = User.query.filter_by(username=user).first()

        if email_exist:
            flash("email already exist!",category='error')
        elif user_exist:
            flash("username is taken!",category="error")
        elif password1 != password2:
            flash("Password does not match!",category="error")
        elif len(email) < 6:
            flash("email not valid", category="error")
        elif len(password1) < 8:
            flash("password is not long enough", category="error")
        elif len(user) < 6:
            flash("username is not long enough! ",category='error')
        
        else:
            #taking all the information and storing it in a variable called new_user
            new_user = User(email=email, username=user, Passwords=generate_password_hash(
                password1, method='sha256'))
            #going to add all this information to the database
            db.session.add(new_user)
            #have to commit the change so the change takes place
            db.session.commit()
            login_user(email_exist,remember=True)
            flash("account has been created!",category="success")

            
    
    return render_template("newuser.html",user= current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))




