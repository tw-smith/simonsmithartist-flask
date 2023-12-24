from artist_app import db
from artist_app.database.models import Cart
from artist_app.stripe_api.products_and_prices import get_price, get_product


def create_cart() -> str:
    cart = Cart()
    db.session.add(cart)
    db.session.commit()  # TODO error handling
    return cart.public_id


def get_cart(cart_id: str) -> Cart:
    cart = db.session.execute(
        db.select(Cart).filter_by(public_id=cart_id)
    ).first()  #TODO not found
    return cart


def get_cart_contents(cart_id: str):
    cart = get_cart(cart_id)
    return cart.contents



def delete_cart():
    pass
