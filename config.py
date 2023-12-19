import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'env'))

class Config(object):
    APP_TITLE = 'Simon Smith Artist'
    CACHE_TYPE = os.environ.get('CACHE_TYPE')
    CACHE_DIR = os.environ.get('CACHE_DIR')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    STRIPE_SECRET_API_KEY_DEV = os.environ.get('STRIPE_SECRET_API_KEY_DEV')
