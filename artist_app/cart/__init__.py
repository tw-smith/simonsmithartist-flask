from flask import Blueprint

bp = Blueprint('cart', __name__, template_folder='templates')

from artist_app.cart import routes