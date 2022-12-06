from app import myapp_obj
from app import db
from app.forms import RegistrationForm, EmptyForm, LoginForm
from flask import render_template, redirect, flash, url_for, request
from app.forms import LoginForm, Search
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from app.forms import PostForm
from app.models import Post
from datetime import datetime
<<<<<<< HEAD
from time import ctime
=======
from app.forms import MessageForm
from app.models import Message
>>>>>>> 6adee8eb4f901ae2a5fecc4522aa1d1951a3da94


@myapp_obj.route('/private')
@login_required
def private():
    return 'Hi this is a private page'

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out. Thank you for visiting!')   #confirmation of logout
    return redirect('/')     #redirect to starting page (LA 12/2 2:32pm)


@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # If user is already logged in redirect to homepage
    if current_user.is_authenticated:
        flash('User is currently logged in! Please logout to login as another user')
        return redirect('/')
    
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
        flash('Successfully Logged In')
        return redirect('/')

    #a = 1
    #name = 'Carlos'
    if current_form.username.data == "" or current_form.password.data == "":
        flash('ERROR: Empty input')
    a = 'Login'
 
    return render_template('login.html', a=a, form=current_form)

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        flash('Please logout before registration')
        return redirect(url_for('homepage'))
    if form.validate_on_submit():
        user = User(username = form.username.data, name = form.name.data, email=form.email.data, num_new_private_messages = 0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
@myapp_obj.route('/')
def homepage():
    return render_template('base.html', current_user=current_user)

#delete account
@myapp_obj.route('/delete')
@login_required
def delete():
    current_user.delete()
    db.session.commit()
    flash('User has been deleted')
    logout_user()
    return redirect('/')
    


@myapp_obj.route('/account')
def account():
    # If user is not logged in request user to log in
    if current_user.is_authenticated is False:
        flash('Account cannot be accessed because User is not logged in')
        return redirect('/')
    # Display profile info
    user = current_user
    form = EmptyForm()
    return render_template("profile.html", user=user, form=form)

@myapp_obj.route('/post', methods=['GET','POST'])
#@myapp_obj.route('/index',methods=['GET','POST'])
@login_required

def index():
    form = PostForm()
    post = Post.query.all()
    user = current_user
    time = datetime.now()
    date_time = time.strftime("%H:%M:%S, %m/%d/%Y")
    if form.validate_on_submit():
        post = Post(body=form.post.data, user_id=current_user.name)
        db.session.add(post)
        db.session.commit()
        flash('Your latest message has been posted!')
        return redirect(url_for('index'))
    #delete below
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]    #fake generated posts (delete later)
    return render_template("post.html", title='Home Page', form=form, post=post, posts=posts, user=user, date_time=date_time ) #renders posting page generated by given html

# Follower user  
@myapp_obj.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:

            flash('User {} not found.'.format(username))
            return redirect(url_for('homepage'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('homepage'))    
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect( url_for('searchProfile', name=username))
    else:
        return redirect(url_for('homepage'))

@myapp_obj.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('homepage'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('homepage')) 
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect( url_for('searchProfile', name=username))
    else:
        return redirect(url_for('homepage'))

@myapp_obj.route('/user/<username>')
@login_required
def user(username):
    form = EmptyForm()
    return render_template('user.html', user=user, form=form)



@myapp_obj.route("/search",methods =['POST','GET'])
@login_required
def search():
    form = Search()
    return render_template("search.html", form = form)

@myapp_obj.route("/searchResult",methods =['POST'])
@login_required
def searchResult():
    current_form = Search()
    name = ""
    user = User.query.filter_by(username=current_form.username.data).first()
    if user is None:
        flash('User does not exist')
    else:
        name = current_form.username.data
    return render_template('searchResult.html', name = name)

@myapp_obj.route("/searchProfile/<name>",methods =['GET'])
@login_required
def searchProfile(name):
    # Display profile info
    form = EmptyForm()
    user = User.query.filter_by(username=name).first()   
    return render_template("searchProfile.html", user=user, form=form)

#send private message
@myapp_obj.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        if current_user.username == recipient:
            flash('Cannot send a private message to yourself')
            return redirect(url_for('searchProfile', name=recipient))
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        db.session.commit()
        if user.num_new_private_messages is None:
            user.zero_new_private_messages()
        else:
            user.increment_num_new_private_messages()
            db.session.commit()
        flash(('Your message has been sent.'))
        return redirect(url_for('send_message',
                      recipient=user.username))
    
    return render_template('send_message.html', title='Send Message',
                           form=form, recipient=recipient)

#view private message
@myapp_obj.route('/messages')
@login_required
def messages():
    db.session.commit()
    current_user.last_message_read_time = datetime.utcnow()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page=page, per_page=myapp_obj.config['POSTS_PER_PAGE'],
            error_out=False)
    next_url = url_for('messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('messages', page=messages.prev_num) \
        if messages.has_prev else None
    current_user.zero_new_private_messages()
    db.session.commit()
    
    return render_template('messages.html', messages=messages,
                           next_url=next_url, prev_url=prev_url, User=User)