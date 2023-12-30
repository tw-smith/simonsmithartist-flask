from flask import Blueprint

bp = Blueprint('stripe_api', __name__, template_folder='templates')

from artist_app.stripe_api import routes