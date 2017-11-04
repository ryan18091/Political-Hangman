import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xc0\xc3\xe42\xb6\x0cl\x93\xfd\x8e\xfd(\xb7\x8de\x9an\x86\x19\xea\x87\xb5\x1f\xea'
    #for local
    SQLALCHEMY_DATABASE_URI = 'sqlite:///political_hangmanPSQL.db'
    #for Heroku
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


    # consumer_key = "tgOf65xyMVuk98JMIJ6o8OV0w"
    # consumer_secret = "FUc8m2bpTIDKK6FoSBYj5jpsC5sG7fcFqS5ZGAuMdLLJqkS7CS"
    # access_token = "2401698925-jgzfZofScmvzyzfUWdxgI9FZuIXmjMrdt3NalJa"
    # access_token_secret = "U8LWL3VwHg4BTAgWWEDLitjrpoRG2MkKoKWTIXgtMKUDn"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False