"""Core functionalities here"""
def init_app(app):
    from movies.core import (
        data_operations,
    )
    data_operations.init_app(app)