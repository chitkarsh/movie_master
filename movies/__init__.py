import argparse
import os
import sys

from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

from movies import (log
                    , routes
                    , core
                    , models
                    , auth
                    )
from movies.config import app_config


db = SQLAlchemy()
# order is important
initiables = [log, db, models, routes, auth, core]


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    try:
        app.config.from_object(app_config[config_name])
    except KeyError:
        RED = '\033[31m'
        RESET = '\033[0m'
        print '{}FLASK_CONFIG not found in environment variable. Define as dev, stage or prod{}'.format(RED,RESET)
        sys.exit()
            
    app.config.from_pyfile('app_config.py')
        
    try:
        with app.app_context():
            for module in initiables:
                module.init_app(app)
        
        return app
    except KeyError as kerr:
        RED = '\033[31m'
        RESET = '\033[0m'
        print '{}{} not found in config{}'.format(RED, kerr.message, RESET)
        sys.exit()

config_name = os.getenv('FLASK_CONFIG')
application = create_app(config_name)
