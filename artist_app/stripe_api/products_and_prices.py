import stripe
from stripe import ListObject, Product, Price
from flask import current_app
from artist_app import cache
from dataclasses import dataclass

#TODO then hit Stripe API again when on product detail page to make sure the product is still available


@dataclass
class ProductPriceObject:
    product: Product
    price_string: str


@cache.cached(timeout=300, key_prefix="product_price")
def get_price(product: Product) -> Price:
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    return stripe.Price.retrieve(product.default_price)


@cache.cached(timeout=300, key_prefix="product")
def get_product(product_id: str) -> Product:
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    return stripe.Product.retrieve(product_id)


@cache.cached(timeout=300, key_prefix="product_list")
def get_all_products() -> ListObject[Product]:
    stripe.api_key = current_app.config['STRIPE_SECRET_API_KEY_DEV']
    return stripe.Product.list(limit=100, active=True) #TODO hasMore check


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


def get_all_products_with_prices() -> [ProductPriceObject]:
    product_price_list = []
    product_list = get_all_products()
    for product in product_list.data:
        price = get_price(product)
        product_price_list.append(
           ProductPriceObject(product=product, price_string=get_price_string(price))
        )
    return product_price_list
