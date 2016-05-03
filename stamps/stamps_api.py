"""
Description: This API is part of the Thinkful Stamps project.
The API is to allow for GET requests that will fetch populated data and save that data in a JSON object.

POST, UPDATE & DELETE requests will come as the data categories are flushed out.
authored by Michael Nickey on February 26th 2016
"""
import json
import logging
import pprint
import os

from flask import Flask, jsonify, abort, make_response, request, render_template,Response
from flask.ext.sqlalchemy import SQLAlchemy
from jsonschema import validate, ValidationError

from . import models, decorators, app
from .database import session

pp = pprint.PrettyPrinter(indent=4)

# Logging Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    stamps = session.query(models.Stamp).all()
    all_stamps = json.dumps([stamp.to_dict() for stamp in stamps])
    return Response(all_stamps, 200, mimetype="application/json")


# Get the stamp by stamp tags
@app.route('/api/stamps/<string:category>/', methods=['GET']) 
def get_stamps_by_tag(category):
        logger.info("in the GET method")
        stamps = session.query(models.Stamp).filter(models.Stamp.tags.contains(category))
        stamps = json.dumps([stamp.to_dict() for stamp in stamps])
        if len(stamps) == 0:
            return Response({"message":"None Found"}, 404, mimetype="application/json")
        return Response(stamps, 200, mimetype="application/json")

@app.route('/api/questions/<string:category>', methods=["GET"])
def get_questions(category):
    questions = session.query(models.Question).filter_by(category=category)
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

