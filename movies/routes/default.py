from flask import request, abort
from flask.blueprints import Blueprint
from movies.log import get_logger
from movies.core.commons import jsonify

logger = get_logger()
mod = Blueprint('default', __name__)


@mod.route('/', methods=['GET'])
def landing_endpoint():
    response = jsonify({'message':'Welcome to the Application. This is an endpoint for sanity test. The app is up and running.' })
    return response

@mod.app_errorhandler(403)
def error_403(e):
    logger.error('{}'.format(e))
    message = 'access forbidden' if not e.description else e.description
    return jsonify({'message':message}),403

@mod.app_errorhandler(404)
def error_404(e):
    return jsonify({'message':'route not found'}),404

@mod.app_errorhandler(401)
def error_401(e):
    logger.error('{}'.format(e))
    message = 'unauthorized' if not e.description else e.description
    return jsonify({'message':message}),401

@mod.app_errorhandler(500)
def error_500(e):
    logger.error('{}'.format(e))
    message = 'server error' if not e.description else e.description
    return jsonify({'message':message}),500

@mod.app_errorhandler(422)
def error_422(e):
    logger.error('{}'.format(e))
    message = 'User Behind the Keyboard Error' if not e.description else e.description
    return jsonify({'message':message}),422
