#!/flask/bin/python

# Database Configuration
import os
from migrate.versioning import api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'stamps.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                        api.version(SQLALCHEMY_MIGRATE_REPO))

class Stamp(Base):
    __tablename__ = 'stamp'
    id = Column(Integer, primary_key=True, index=True)
    state = Column(String(30))
    state_abbr = Column(String(2))
    stamp_name = Column(String(100))
    blurb = Column(String(500))
    date_issued = Column(String(20))
    country = Column(String(20))
    value = Column(Float(10))

    def to_dict(self):
        return {"id": self.id, "state": self.state,
                "state_abbr": self.state_abbr, "stamp_name": self.stamp_name,
                "blurb": self.blurb, "date_issued": self.date_issued,
                "country": self.country, "value": self.value}

Base.metadata.create_all(bind=engine)
Base.query = db_session.query_property()
conn = engine.connect()