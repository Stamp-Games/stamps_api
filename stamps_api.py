#!flask/bin/python

"""
Description: This API is part of the Thinkful Stamps project.
The API is to allow for GET requests that will fetch populated data and save that data in a JSON object.

POST, UPDATE & DELETE requests will come as the data categories are flushed out.
authored by Michael Nickey on February 26th 2016
"""

from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/api/stamps/', methods=['GET'])
def get_stamps():
    return jsonify({'stamps': stamps})


if __name__ == '__main__':
    app.run(debug=True)