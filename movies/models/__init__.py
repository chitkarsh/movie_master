"""Data models and resource abstractions."""

def init_app(app):
    from movies.models import (
        movie_model,
        user_model,
    )
    movie_model.init_app(app)
    #user_model.init_app(app)
    