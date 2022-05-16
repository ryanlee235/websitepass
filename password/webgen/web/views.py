from flask import Blueprint, render_template, request, flash, url_for,redirect
from flask_login import login_required, current_user
from .models import User, Passwords
from. import db
import random 
import os 
views = Blueprint('views',__name__)


@views.route("/generate")

def userinfo():
    return render_template('generate.html')
@views.route('/')
@views.route('/home',methods = ['GET','POST'])
def generate_password():
    if request.method == "POST":
        website = request.form.get('website')

        
        website_exists = Passwords.query.filter_by(website=website).first()
        if len(website_exists) < 1:
            flash("Enter website name to generate password",category="error")
        elif website_exists:
            upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lower_letters = upper_letters.lower()
            symbols ='!@#$%^&*()?<>/:;'
            num = '12345678'

           
            all = upper_letters + lower_letters +symbols + num
            
            length = 12
    
            
            password = ''.join(random.sample(all,length))
                
            new_password = Passwords(Passwords=password,website=website)
                
            db.session.add(new_password)
            db.session.commit()
            flash("password successfully added!")

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
    
