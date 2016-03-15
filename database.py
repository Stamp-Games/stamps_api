#!/flask/bin/python

# Database Configuration
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'stamps.db')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class Stamp(Base):
    __tablename__ = 'stamp'
    id = Column(Integer, primary_key=True, index=True)
    state = Column(String(30))
    state_abbr = Column(String(2))
    stamp_url = Column(String(300))
    stamp_name = Column(String(100))
    blurb = Column(String(500))
    date_issued = Column(String(20))
    country = Column(String(20))
    value = Column(Float(10))

    def to_dict(self):
        return {"id": self.id, "state": self.state, "stamp_url": self.stamp_url,
                "state_abbr": self.state_abbr, "stamp_name": self.stamp_name,
                "blurb": self.blurb, "date_issued": self.date_issued,
                "country": self.country, "value": self.value}

Base.metadata.create_all(bind=engine)
Base.query = db_session.query_property()
conn = engine.connect()
