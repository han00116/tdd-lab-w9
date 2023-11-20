# src/__init__.py

import os  # new

from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong! pong pong'
        }
#import sys
#print(app.config, file=sys.stderr)

api.add_resource(Ping, '/ping')
