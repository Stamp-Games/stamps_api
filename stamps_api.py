#!flask/bin/python

"""
Description: This API is part of the Thinkful Stamps project.
The API is to allow for GET requests that will fetch populated data and save that data in a JSON object.

POST, UPDATE & DELETE requests will come as the data categories are flushed out.
authored by Michael Nickey on February 26th 2016
"""
# Todo(mnickey) : Add support to database to hold stamps rather than hard-coding them
# Todo(mnickey) : create database seed entries
# Todo(mnickey) : revamp endpoints to use SQLAlchemy
# Todo(mnickey) : create POST request endpoint
# Todo(mnickey) : create UPDATE endpoint
# Todo(mnickey) : create DELETE endpoint

import logging
from flask import Flask, jsonify, abort, make_response, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI

# Traceback error seen here -- need to resolve also tried `import models`
# Traceback also mentions from stamps_api import db on models.py file
# from . import Stamp

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()
conn = engine.connect()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# new_stamp = Stamp()
# new_stamp.name = 'my_name'
# new_stamp.origin = 'my_orgin'
# new_stamp.rarity = 'my_rarity'
#
# db.session.add(new_stamp)
# db.session.commit()

# Logging Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

version = 1
stamps = [
    {
        "id": 1,
        "name": "My first stamp",
        "orgin": "Unicorn Nightmares",
        "rarity": "very rare"
    },
    {
        "id": 2,
        "name": "My second Stanp",
        "orgin": "Heavens Breath",
        "rarity": "common"
    }
]

"""
DATABASE FUNCTIONS
"""
def init_db():
    Base.metadata.create_all(bind=engine)


def query_db():
    from models import Stamp
    Stamp.query.all()

"""
API CALLS
"""
# Get all the stamps
@app.route('/api/stamps/', methods=['GET'])
def get_stamps():
    return jsonify({'stamps': stamps[:]})


# Get the stamp by stamp ID
@app.route('/api/stamps/<int:stamp_id>/', methods=['GET'])
def get_stamps_by_id(stamp_id):
    logger.info('\nCollecting matching stamp...')
    stamp = [stamp for stamp in stamps if stamp['id'] == stamp_id]
    if len(stamp) == 0:
        abort(404)
    return jsonify({'stamps': stamp})


# Error handling for stamps not found by API request
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
    init_db()
    query_db()
