from app import myapp_obj
from app import db
from app.forms import RegistrationForm
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user


@myapp_obj.route('/private')
@login_required
def private():
    return 'Hi this is a private page'

@myapp_obj.route('/logout')
@login_required
def logout():
    load_user(current_user)
    return redirect('/')


@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()
        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')

    #a = 1
    #name = 'Carlos'
    if current_form.username.data == "" or current_form.password.data == "":
        flash('ERROR: Empty input')
    a = 'Welcome to my App!'
    name = 'User'
 
    return render_template('login.html', name=name, a=a, form=current_form)

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
@myapp_obj.route('/')
def home():
    return render_template('home.html')

@myapp_obj.route('/table')
def users():
    all_users = User.query.all()
    return render_template("table.html", form=all_users)
