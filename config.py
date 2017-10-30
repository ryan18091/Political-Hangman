import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    SQLALCHEMY_DATABASE_URI = os.environ['sqlite:///political_hangmanPSQL.db']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = Fals