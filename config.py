import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    APP_TITLE = 'Simon Smith Artist'
    CACHE_TYPE = os.environ.get('CACHE_TYPE')
    CACHE_DIR = os.environ.get('CACHE_DIR')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'artist_app/database/db_prod.database')


class DevConfig(Config):
    STRIPE_SECRET_API_KEY_DEV = os.environ.get('STRIPE_SECRET_API_KEY_DEV')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'artist_app/database/db_dev.db')


class TestConfig(Config):
    TESTING = True
    CACHE_TYPE = "NullCache"
    STRIPE_SECRET_API_KEY_DEV = os.environ.get('STRIPE_SECRET_API_KEY_DEV')
