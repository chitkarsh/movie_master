from flask import abort
from flask.views import MethodView
from werkzeug.security import safe_str_cmp
from datetime import datetime, timedelta
from movies.models.user_model import *

class Authentication(MethodView):
    
    @staticmethod
    def make_payload(identity):
        iat = datetime.utcnow()
        exp = iat + timedelta(seconds=300)
        nbf = iat + timedelta(seconds=0)
        identity =identity.key.urlsafe()
        return {'exp':exp,'iat': iat, 'nbf': nbf, 'identity': identity}

    @staticmethod
    def authenticate(username,password):
        user=username_table.get(username,None)
        if user and safe_str_cmp(user.password.encode('utf-8'),password.encode('utf-8')):
            return user
        else:
            abort(401)

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = userid_table.get(user_id,None)
        if not user:
            abort(401)
        return user