import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class PRODUCTION(Config):
    DEBUG = False
