from dataclasses import dataclass
from flask import session
from artist_app.cart import bp
from artist_app.database.services import create_cart, get_cart, get_cart_mapping
from artist_app.database.models import Cart, CartItem
from artist_app.stripe_api.products_and_prices import get_price, get_product


@bp.route('/cart/add/<product_id>', methods=['POST'])
def add_item_to_cart(product_id):
    print(f"Start request session{session}")
    cart_id = session.get('cart_id')
    if cart_id is None:
        print("creating new cart")
        session['cart_id'] = create_cart()
    print(session)
    cart: Cart = get_cart_mapping(session['cart_id'])
    return cart.add_item_to_cart(product_id)


@bp.route('/cart/remove/<product_id>', methods=['POST'])
def remove_item_from_cart(product_id):
    cart_id = session.get('cart_id')
    if cart_id is None:
        return 'No cart exists'
    cart: Cart = get_cart_mapping(session['cart_id'])
    return cart.remove_item_from_cart(product_id)

@bp.route('/cart', methods=['GET'])
def get_cart():
    cart_id = session.get('cart_id')
    if cart_id is None:
        return 'No cart exists'
    cart: Cart = get_cart_mapping(cart_id)
    return cart.to_dict()

    #return {'cart_total': session['cart'].get_cart_total()} # TODO handle strip no such product error

