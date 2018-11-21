from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
import pymysql
from flask_cors import *


app = Flask(__name__)
app.debug = True
app.secret_key = "welecome to hubwebpage"
app.config.from_pyfile('config.py', silent=True)

login_manager = LoginManager(app)
login_manager.init_app(app)
bootstrap = Bootstrap(app)
CORS(app, supports_credentials=True)


db = SQLAlchemy(app)
from .models import User, Member, Essay, Project
migrate = Migrate(app, db)

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Member=Member, Essay=Essay, Project=Project)


manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))

from . import views
