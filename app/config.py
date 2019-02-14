""" Defines runtime environment configurations """

# Standard import
import os


class Config:
    """ Define common configurations for all environments """
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    """ Defines configurations for testing """

    TESTING = True
    DATABASE_URL = 'postgresql://postgres:star2030@localhost/testdb_politico'


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
