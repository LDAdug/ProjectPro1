from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from app import login
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15))
    name = db.Column(db.String(15))
    password = db.Column(db.String(200))
    email = db.Column(db.String(32), unique = True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def delete(self):
        db.session.delete(self)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login.user_loader 
def load_user(id):
    return User.query.get(int(id))
    