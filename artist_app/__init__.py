import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_caching import Cache
from config import Config, DevConfig, ProdConfig


cache = Cache()

def create_app(config_class=Config):
    app = Flask(__name__)
    if app.debug:
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(ProdConfig)
    from artist_app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/arcade.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)

    cache.init_app(app)
    return app
