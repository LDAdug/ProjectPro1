from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm


@myapp_obj.route('/', methods=['POST', 'GET'])
def home():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    if current_form.username.data == "" or current_form.password.data == "":
        flash('ERROR: Empty input')
    a = 'Welcome to my App!'
    name = 'User'
    return render_template('login.html', name=name, a=a, form=current_form)
