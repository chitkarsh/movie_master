
def init_app(app):
    from movies.routes import (
        admin_handler,
        user_handler,
        default,
    )

    app.register_blueprint(admin_handler.mod)
    app.register_blueprint(user_handler.mod)
    app.register_blueprint(default.mod)
   