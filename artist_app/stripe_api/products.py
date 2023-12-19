import stripe
from stripe import ListObject, Product, Price
from flask import current_app
from artist_app import cache
#TODO rather than hitting the Stripe API every time, use flask-caching to cache product and price list on first home
# page visit then hit Stripe API again when on product detail page to make sure the product is still available


@cache.cached(timeout=300, key_prefix="all_products")
def get_all_products() -> ListObject[Product]:
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    product_list = stripe.Product.list(limit=100, active=True) #TODO hasMore check
    return product_list


def get_price_string(price: Price) -> str:
    if price.currency == 'gbp':
        currency_string = '£'
    elif price.currency == 'usd':
        currency_string = '$'
    elif price.currency == 'eur':
        currency_string = '€'
    else:
        currency_string = ''
    return f"{currency_string}{(price.unit_amount/100):.2f}"



def get_all_products_with_prices() -> list:  # TODO improve this type checking
    product_price_list = []
    product_list = get_all_products()
    for product in product_list.data:
        price = get_product_price(product)
        product_price_list.append({
            'product': product,
            'price_string': get_price_string(price)
        })
    return product_price_list


@cache.cached(timeout=300, key_prefix="product_price")
def get_product_price(product: Product) -> Price:
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    price = stripe.Price.retrieve(product.default_price)
    return price


def get_product_and_price(product_id: str) -> [Product, Price]:
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    product = stripe.Product.retrieve(product_id)
    price = get_product_price(product)
    return product, price
