import os
from datetime import datetime


"""
Description: This API is part of the Thinkful Stamps project.
The API is to allow for GET requests that will fetch populated data and save that data in a JSON object.

POST, UPDATE & DELETE requests will come as the data categories are flushed out.
authored by Michael Nickey on February 26th 2016
"""
import json
import logging

from flask import Flask, jsonify, abort, make_response, request, render_template,Response
from flask.ext.sqlalchemy import SQLAlchemy
from jsonschema import validate, ValidationError
from sqlalchemy import create_engine, Table, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
# Logging Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(app.config["DATABASE_URI"])
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

"""
Models
"""
class Stamp(Base):
    __tablename__ = 'stamps'
    
    id = Column(Integer, primary_key=True, index=True)
    
    stamp_name = Column(String(30))
    stamp_url = Column(String(300))
    blurb = Column(String(500),default='')
    date_issued = Column(String(20),default='')
    value = Column(Float(10), default=0)
    tags = Column(String(1000))

    def to_dict(self):
        return {"id": self.id, 
                "stamp_url": self.stamp_url,
                "stamp_name": self.stamp_name,
                "blurb": self.blurb, 
                "date_issued": self.date_issued,
                "tags": self.tags.split(','), 
                "value": self.value
        }

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(20))
    image = Column(String(500))
    body = Column(String(1024))
    correct_answer = Column(String(100))
    answers = Column(String(1024))
    
    def to_dict(self):
        return {
            "id":self.id,
            "category":self.category,
            "image":self.image,
            "body":self.body,
            "correct answer":self.correct_answer,
            "answers":self.answers.split(',')
            }
"""
WEB PAGES
"""
@app.route('/', methods=['GET'])
@app.route('/stamps/index/', methods=['GET'])
def show_index():
    return render_template('main.html')

"""
API CALLS
"""


# Get all the stamps
@app.route('/api/stamps/', methods=['GET'])
def get_stamps():
    stamps = session.query(Stamp).all()
    all_stamps = json.dumps([stamp.to_dict() for stamp in stamps])
    return Response(all_stamps, 200, mimetype="application/json")


# Get the stamp by stamp tags
@app.route('/api/stamps/<string:category>/', methods=['GET']) 
def get_stamps_by_tag(category):
        logger.info("in the GET method")
        stamps = session.query(Stamp).filter(Stamp.tags.contains(category))
        stamps = json.dumps([stamp.to_dict() for stamp in stamps])
        if len(stamps) == 0:
            return Response({"message":"None Found"}, 404, mimetype="application/json")
        return Response(stamps, 200, mimetype="application/json")

@app.route('/api/questions/<string:category>', methods=["GET"])
def get_questions(category):
    questions = session.query(Question).filter_by(category=category)
    data = json.dumps([question.to_dict() for question in questions ])
    return Response(data, 200, mimetype="application/json")
    
    
# Error handling for stamps not found by API request
@app.errorhandler(404)
def not_found(error=404):
    return make_response(jsonify({'error': 'Not Found'}), 404)


# Get stamps by value -- greater than or equal to the variable in the url
# @app.route('/api/stamps/value/<value>/', methods=['GET'])
# def get_stamps_by_value(value):
#     logger.info("Collecting stamps by value greater or equal to " + value + ".")
#     stamp = [stamp for stamp in all_stamps if str(stamp['value']) >= value]
#     if len(stamp) == 0:
#         abort(404)
#     return json.dumps({'stamp': stamp}, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    app.run()
