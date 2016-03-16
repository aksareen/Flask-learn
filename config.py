#defualt config
import os
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "ajsb24e331e5cejhDKn24m35m3vSFDHf989fe51avSFef1"
    SQLALCHEMY_DATABASE_URI  = 'sqlite:///posts.db'#os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True 


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProdcutionConfig(BaseConfig):
    DEBUG = False