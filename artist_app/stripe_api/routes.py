import stripe
from flask import session, redirect, current_app, render_template, request
from artist_app.stripe_api import bp
from artist_app.database.services import get_cart_mapping
from artist_app.stripe_api.products_and_prices import get_product

@bp.route('/create-stripe-checkout-session', methods=['POST'])
def create_stripe_checkout_session():
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    cart_id = session.get('cart_id')
    if cart_id is None:
        return 'No cart exists'
    cart = get_cart_mapping(cart_id)
    line_items = []
    for item in cart.contents:
        product_object = get_product(item.product_id) # TODO maybe refactor to have price id in cart contents object
        line_item = {
            'price': product_object.default_price,
            'quantity': item.quantity
        }
        line_items.append(line_item)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=request.url_root + '/success',
            cancel_url=request.url_root + '/cancel'
        )
    except Exception as e:
        return str(e)
    print(checkout_session)
    return redirect(checkout_session.url, 303)

@bp.route('/checkout', methods=['GET'])
def checkout():
    return render_template('checkout.html')