import os
from logging import WARNING, INFO, DEBUG
from datetime import timedelta

class Config(object):
    '''
    Common configurations
    '''
    APP_NAME = 'movies'
    LOG_FILE = 'movies.log'
    JWT_ALGORITHM ='HS256'
    JWT_AUTH_URL_RULE = '/auth'
    JWT_EXPIRATION_DELTA = timedelta(seconds=300) #5 mins


class DevelopmentConfig(Config):
    '''
    Development configurations
    '''
    LOG_LEVEL = DEBUG
    DEBUG = True
    SQLALCHEMY_ECHO = True

class StageConfig(Config):
    '''
    Stage configurations
    '''
    LOG_LEVEL = DEBUG
    DEBUG = False

class ProductionConfig(Config):
    '''
    Production configurations
    '''
    LOG_LEVEL = WARNING
    DEBUG = False

app_config = {
    'dev': DevelopmentConfig,
    'stage': StageConfig,
    'prod': ProductionConfig
}
