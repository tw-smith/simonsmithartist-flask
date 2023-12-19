from flask import render_template, current_app
from artist_app.main import bp
from artist_app.stripe_api.products import get_all_products, get_product_and_price, get_all_products_with_prices, get_price_string





@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html', product_list=get_all_products())

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@bp.route('/latest', methods=['GET'])
def product_index():
    product_price_list = get_all_products_with_prices()
    return render_template('product_index.html', product_list=product_price_list)

@bp.route('/product/<product_id>', methods=['GET'])
def product_page(product_id: str):
    product, price = get_product_and_price(product_id)
    price_string = get_price_string(price)
    return render_template('product_page.html', product=product, price_string=price_string)
