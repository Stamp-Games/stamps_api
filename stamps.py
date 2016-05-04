import os

from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
config_path = os.environ.get("CONFIG_PATH", "stamps.config.DevelopmentConfig")
app.config.from_object(config_path)

from stamps import stamps_api
from stamps.database import Base, engine

Base.metadata.create_all(engine)

def run():
    port = int(os.environ.get('PORT',8080))
    app.run(host="0.0.0.0",port=port)
    
if __name__ == "__main__":
    print("called run")
    run()