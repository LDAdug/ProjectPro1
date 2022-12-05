from flask import Flask
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.update(
    SECRET_KEY='this-is-a-secret',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(myapp_obj)
login = LoginManager(myapp_obj)

migrate = Migrate(myapp_obj, db)

login.login_view = 'login'

with myapp_obj.app_context():
    db.create_all()
    
from app import routes, models