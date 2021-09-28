from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import User, Passwords
from. import db
import random 
import os 
views = Blueprint('views',__name__)
@views.route('/')
@views.route('/home')
# home will display our user info, this will also  display the passwords for the user and website they are using for the passwords
def home():
    return render_template('home.html', user= current_user)

@views.route("/generate")

def userinfo():
    return render_template('generate.html')

@views.route('/create-password',methods = ['GET','POST'])
def generate_password():
    if request.method == "POST":
        website = request.form.get('website')
        
        website_exists = Passwords.query.filter_by(website=website).first()
        if website_exists:
            upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lower_letters = upper_letters.lower()
            symbols ='!@#$%^&*()?<>/:;'
            num = '12345678'

            all=""
            all = upper_letters + lower_letters +symbols + num
            amount = 1
            length = 12
                

            for x in range(amount):
                password = ''.join(random.sample(all,length))
                
                new_password = Passwords(Passwords=password)
                
                db.session.add(new_password)
                db.session.commit()
                flash("password successfully added!")


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

@views.route('/website-name/<website>', methods = ['GET', 'POST'])
def website():
    if request.method == "POST":
        website  = request.form.get('')
        db.session.add(website)
        db.session.commit()
