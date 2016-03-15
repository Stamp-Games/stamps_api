# # Database Configuration
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.ext.declarative import declarative_base
#
# # Database Setup
# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'stamps.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
# Base = declarative_base()
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Base.metadata.create_all(bind=engine)
# Base.query = db_session.query_property()
# conn = engine.connect()
