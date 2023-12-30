import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from config import Config, DevConfig, ProdConfig, TestConfig


cache = Cache()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    # app.config.from_object(config_class)
    if app.debug:
        app.config.from_object(DevConfig)
    elif app.testing:
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(ProdConfig)
    from artist_app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from artist_app.cart import bp as cart_bp
    app.register_blueprint(cart_bp)

    from artist_app.stripe_api import bp as stripe_api_bp
    app.register_blueprint(stripe_api_bp)

    if not app.debug and not app.testing:

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/arcade.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)




    return app
