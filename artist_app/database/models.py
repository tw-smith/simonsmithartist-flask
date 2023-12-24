import uuid
from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as so
from artist_app import db
from artist_app.stripe_api.products_and_prices import get_price, get_product


class Cart(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    public_id: so.Mapped[str] = so.mapped_column(sa.String(60), index=True, unique=True)
    total: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0)
    contents: so.Mapped[List["CartItem"]] = so.relationship(back_populates="parent_cart")

    def __init__(self, public_id: str):
        self.public_id = public_id

    def add_item_to_cart(self, product_id: str):
        cart_item: CartItem = self.search_cart_contents(product_id)
        if cart_item:
            cart_item.increase_quantity()
        else:
            new_cart_item = CartItem(product_id, self.id)
            db.session.add(new_cart_item)
        self.refresh_cart_total()
        db.session.commit()
        return self.to_dict()

    def remove_item_from_cart(self, product_id: str):
        cart_item: CartItem = self.search_cart_contents(product_id)
        if cart_item:
            cart_item.decrease_quantity()
        self.refresh_cart_total()
        db.session.commit()
        return self.to_dict()

    def search_cart_contents(self, product_id: str):
        item = next((x for x in self.contents if x.product_id == product_id), None)
        return item

    def refresh_cart_total(self):
        new_total = 0.0
        print(self.contents)
        for item in self.contents:
            print(f"Item price: {item.price}")
            print(f"Item quant: {item.quantity}")
            new_total += item.price * item.quantity
        self.total = new_total

    def to_dict(self):
        contents_list = []
        for item in self.contents:
            contents_list.append(item.to_dict())
        cart_obj_repr = {
            'cart_id': self.public_id,
            'total': self.total,
            'contents': contents_list
        }
        return cart_obj_repr

    def __repr__(self):
        return '<Cart {}>'.format(self.public_id)


class CartItem(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    cart_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("cart.id"))
    parent_cart: so.Mapped["Cart"] = so.relationship(back_populates="contents")
    name: so.Mapped[str] = so.mapped_column(sa.String(120))
    product_id: so.Mapped[str] = so.mapped_column(sa.String(60))
    price: so.Mapped[float] = so.mapped_column(sa.Float)
    quantity: so.Mapped[int] = so.mapped_column(sa.Integer, default=1)

    def __init__(self, product_id: str, cart_id: int):
        product_object = get_product(product_id)
        price_object = get_price(product_object)
        self.name = product_object.name
        self.product_id = product_id
        self.price = price_object.unit_amount / 100
        self.cart_id = cart_id
        self.parent_cart = db.session.get(Cart, self.cart_id)
        self.quantity = 1

    def increase_quantity(self):
        self.quantity += 1

    def decrease_quantity(self):
        self.quantity -= 1
        if self.quantity < 0:
            self.quantity = 0
        if self.quantity == 0:
            cart_item = db.session.get(CartItem, self.id)
            db.session.delete(cart_item)
            db.session.commit()


    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

    def __repr__(self):
        return '<CartItem {}>'.format(self.name)
