import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from stamps import app

engine = create_engine(app.config["DATABASE_URI"])
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
