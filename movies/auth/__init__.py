from flask_jwt import JWT


def init_app(app):
    from movies.auth import (
        jwt_auth_util,
    )
    JWT(app, jwt_auth_util.Authentication.authenticate,
        jwt_auth_util.Authentication.identity)
