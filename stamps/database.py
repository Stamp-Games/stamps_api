#!/flask/bin/python

# Database Configuration
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float

from . import app

engine = create_engine(app.config["DATABASE_URI"])
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Base.metadata.create_all(bind=engine)
# Base.query = db_session.query_property()
# conn = engine.connect()
