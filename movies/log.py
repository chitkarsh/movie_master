import logging
from logging.handlers import RotatingFileHandler

def get_logger():
    return logging.getLogger(appname)

def init_app(app):
    global appname, web_log_handler
    appname = app.name
    handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=1000000, backupCount=5)
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])
    
    # initializing below logger for request logging
    # doesn't logs with external servers
    request_logger = logging.getLogger('werkzeug')
    request_logger.addHandler(handler)
    if app.debug:
        console_handler = logging.StreamHandler()
        request_logger.addHandler(console_handler)
   