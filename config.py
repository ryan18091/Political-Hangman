import os


# default config
class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['sqlite:///political_hangmanPSQL.db']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False