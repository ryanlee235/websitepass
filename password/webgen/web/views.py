from flask import Blueprint, render_template, request, flash, url_for,redirect
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
                
            
            password_gen = Passwords(password=password, website=website) 
            db.session.add(password_gen)
            db.session.commit()
            flash("password generated successfully",category="success")

    return render_template("home.html",user=current_user)
        

@views.route('/delete-password/<id>')
def delete():
    password = Passwords.query.filter_by(id=id).first()
    
    if not password:
        flash("password does not exist! ", category ="error")
    elif current_user.id != password.id:
        flash("you do not have permission to delete this password", category='error')
    else:
        db.session.delete(password)
        db.session.commit()
        flash("password successfully deleted! ")
    
