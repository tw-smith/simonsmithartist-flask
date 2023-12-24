from dataclasses import dataclass
from flask import session
from artist_app.cart import bp
from artist_app.database.services import create_cart, get_cart_contents, get_cart
from artist_app.database.models import Cart, CartItem
from artist_app.stripe_api.products_and_prices import get_price, get_product

#
# class CartItem:
#     def __init__(self, product_id: str):
#         self.product_id = product_id
#         product_object = get_product(product_id)
#         price_object = get_price(product_object)
#         price_number = price_object.unit_amount / 100
#         self.price = price_number
#         self.quantity = 1
#         self.name = product_object.name
#
#     def increase_quantity(self):
#         self.quantity += 1
#
#     def decrease_quantity(self):
#         self.quantity -= 1
#         if self.quantity < 0:
#             self.quantity = 0
#
#     def get_quantity(self):
#         return self.quantity
#
#
#
# class Cart:
#     def __init__(self):
#         self.cart_items = []
#         self.total = 0
#
#     def find_item(self, product_id):
#         item = next((x for x in self.cart_items if x['product_id'] == product_id), None)
#         return item
#
#     def add_item(self, product_id):
#         cart_item = self.find_item(product_id)
#         if cart_item:
#             #cart_item.increase_quantity()
#             cart_item['quantity'] += 1
#         else:
#             #cart_item: CartItem = CartItem(product_id)
#             product_object = get_product(product_id)
#             price_object = get_price(product_object)
#             price_number = price_object.unit_amount / 100
#             name = product_object.name
#             cart_item = {
#                 'product_id': product_id,
#                 'name': name,
#                 'price': price_number,
#                 'quantity': 1
#             }
#             self.cart_items.append(cart_item)
#         self.refresh_cart_total()
#
#     def remove_item(self, product_id):
#         cart_item = self.find_item(product_id)
#        # cart_item.decrease_quantity()
#         cart_item['quantity'] -= 1
#         #if cart_item.get_quantity() == 0:
#         if cart_item['quantity'] == 0:
#             self.cart_items.remove(cart_item)
#         self.refresh_cart_total()
#
#     def refresh_cart_total(self):
#         new_total = 0
#         for item in self.cart_items:
#             new_total += (item['price'] * item['quantity'])
#         self.total = new_total
#
#     def get_cart_total(self):
#         return self.total


@bp.route('/cart/add/<product_id>', methods=['POST'])
def add_item_to_cart(product_id):
    if 'cart_id' not in session:
        session['cart_id'] = create_cart()
    cart: Cart = get_cart(session['cart_id'])
    print(type(cart))
    cart2: Cart = cart._mapping['Cart']
    out = cart2.add_item_to_cart(product_id)
    return out

    #return {'cart_total': session['cart'].get_cart_total()} # TODO handle strip no such product error


#
# @bp.route('/carts', methods=['POST'])
# def new_cart():
#     public_id = create_cart()
#     session['cart'] = {
#         'cart_id': public_id,
#         'cart_items': []
#     }
#     return public_id, session['cart']
#
#
# @bp.route('/carts/<cart_id>', methods=['GET'])
# def get_cart_contents():
#     contents = session['cart'].cart_items
#     return contents
#
#
#
# @bp.route('/carts/<cart_id>/items', methods=['POST'])
# def add_item_to_cart(product_id: str):
#     if 'cart' not in session:
#         _, _ = new_cart()
#     session['cart'].cart_items.append({
#         'product_id': product_id,
#         'quantity': 1 # TODO remove this hardcoded quantity
#     })
#
#
#
#
# @bp.route('/carts/<cart_id>/items', methods=['GET'])
# def view_cart_items(cart_id: str):
#     pass
