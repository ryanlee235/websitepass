from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import User, Passwords
from. import db
import random 
views = Blueprint('views',__name__)
@views.route('/')
@views.route('/home')
# home will display our user info, this will also  display the passwords for the user and website they are using for the passwords
def home():
    pw = Passwords.query.all()
    return render_template('home.html', user= current_user, password=pw)


@views.route('/create-password',methods = ['GET','POST'])
def generate_password(length,upper,lower,nums,syms):
    if request.method == "POST":
        pw = request.form.get()

        password_exist = Passwords.query.filter_by(password = pw)

        if password_exist:
            flash("password already exist!", category='error')
        else:
            flash("password does not exist!", category="error")
    
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_letters = upper_letters.lower()
        symbols ='!@#$%^&*()?<>/:;'
        num = '12345678'

        all=""
        if upper:
            all+= upper_letters
        if lower:
            all += lower_letters
        if nums:
            all+= num
        if syms:
            all+= symbols 

            
        amount = 1
            

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
        website  = request.form.get()
        website_exist = Passwords.query.filter_by()
