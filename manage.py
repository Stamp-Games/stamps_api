import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from getpass import getpass
from werkzeug.security import generate_password_hash

from blog import app
from blog.database import session, Entry, User, Base


manager = Manager(app)

@manager.command
def seed():
    """ seed DB with dummy entries """
    
        
    # session.add(entry)
    # session.commit()
    pass

@manager.command
def adduser():
    """ adds user to the DB via terminal """
    name = input("Name: ")
    email = input("Email: ")
    if session.query(User).filter_by(email=email).first():
        print("User with that email already exists")
        return
    password = ''
    while len(password) < 8 or password != password_2:
        password = getpass("Password: ")
        password_2 = getpass("Re-enter password: ")
    user = User(name=name, email=email, 
    password=generate_password_hash(password))
    session.add(user)
    session.commit()
    
class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata
migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db',MigrateCommand)

    