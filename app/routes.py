# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@myapp_obj.route('/',methods=['POST','GET'])
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
    a = ' '
    name = 'New User '
    return render_template('login.html', name=name, a=a, form=current_form)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)