""" Defines runtime environment configurations """

# Standard import
import os


class Config:
    """ Define common configurations for all environments """
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    NEW_ADMIN = os.getenv('ADMIN')


class TestingConfig(Config):
    """ Defines configurations for testing """

    TESTING = True
    DATABASE_URL = os.getenv('TEST_DATABASE_URL')

class DevelopmentConfig(Config):
    """ Defines configurations for development """

    DEBUG = True


class ProductionConfig(Config):
    """ Defines configurations for production """

    TESTING = False
    DEBUG = False


APP_CONFIG = dict(
    testing=TestingConfig,
    development=DevelopmentConfig,
    production=ProductionConfig
)
