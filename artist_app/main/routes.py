from flask import render_template, current_app
from stripe import Product, Price
from artist_app.main import bp
from artist_app.stripe_api.products_and_prices import ProductPriceObject
from artist_app.stripe_api.products_and_prices import get_all_products_with_prices, get_price_string, get_product, get_price


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@bp.route('/latest', methods=['GET'])
def product_index():
    product_price_list: [ProductPriceObject] = get_all_products_with_prices()
    return render_template('product_index.html', product_list=product_price_list)


@bp.route('/product/<product_id>', methods=['GET'])
def product_page(product_id: str):
    product: Product = get_product(product_id)
    price: Price = get_price(product)
    price_string = get_price_string(price)
    return render_template('product_page.html', product=product, price_string=price_string)
