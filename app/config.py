import os

super_secret = os.getenv('SECRETE')


class Config:
    """ Define common configurations for all environments """

    SECRET = super_secret


class TestingConfig(Config):
    """ Defines configurations for testing """

    TESTING = True


class DevelopmentConfig(Config):
    """ Defines configurations for development """

    DEBUG = True


class ProductionConfig(Config):
    """ Defines configurations for production """

    pass


app_config = dict(
    testing=TestingConfig,
    development=DevelopmentConfig,
    production=ProductionConfig
)
