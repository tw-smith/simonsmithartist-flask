from artist_app import db
from artist_app.database.models import Cart


def create_cart() -> str:
    cart = Cart()
    db.session.add(cart)
    db.session.commit()  # TODO error handling
    return cart.public_id


def get_cart(public_id: str) -> Cart:
    cart = db.session.execute(
        db.select(Cart).filter_by(public_id=public_id)
    ).first()  #TODO not found
    return cart


def get_cart_contents(public_id: str):
    cart = get_cart(public_id)
    return cart.contents


def add_item_to_cart():
    pass



def remove_item_from_cart():
    pass



def delete_cart():
    pass
