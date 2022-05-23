from flask import Blueprint, render_template, request, flash, url_for,redirect, session
from flask_login import login_required, current_user
from .models import User, Passwords
from. import db
import random 
import os 
views = Blueprint('views',__name__)


@views.route('/')
@views.route('/home',methods = ['GET','POST'])
@login_required
def home():
    if request.method == "POST":
        website = request.form.get("website")
        if len(website) < 1:
            flash("please enter a website name to generate password!", category="error")
        else:
            upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lower_letters = upper_letters.lower()
            symbols ='!@#$%^&*()?<>/:;'
            num = '12345678'

           
            all = upper_letters + lower_letters +symbols + num
            
            length = 12
    
            
            password = ''.join(random.sample(all,length))
                
            
            password_gen = Passwords(websites=website, user_passwords=password)
            db.session.add(password_gen)
            db.session.commit()
            flash("password generated successfully",category="success")


    return render_template("home.html",user=current_user)


@views.route("/userinfo")
def display_info():
    ps1 = Passwords.query.all()

    return render_template("userinfo.html",ps1=ps1,user = current_user)
   
        

@views.route('/delete/<id>')
@login_required
def delete(id):
   password_delete = Passwords.query.get_or_404(id)

   try:
       db.session.delete(password_delete)
       db.session.commit()
       return redirect("/userinfo")
   except:
        return "There was a problem delete the password"

    

