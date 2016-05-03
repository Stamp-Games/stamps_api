import os

from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
config_path = os.environ.get("CONFIG_PATH", "stamps.config.DevelopmentConfig")
app.config.from_object(config_path)

from . import stamps_api
from .database import Base, engine

Base.metadata.create_all(engine)