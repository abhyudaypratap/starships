import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "K2kppfJnuK8@OK!LCnJt*7*hd8VA&EUa7FJC$b"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
