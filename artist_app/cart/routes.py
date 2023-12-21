from artist_app.cart import bp
from artist_app.database.services import create_cart, get_cart_contents

@bp.route('/carts', methods=['POST'])
def new_cart():
    public_id = create_cart()


@bp.route('/carts/<cart_id>', methods=['GET'])
def get_cart_contents(cart_id: str):
    contents = get_cart_contents(cart_id)
    return contents



@bp.route('/carts/<cart_id>/items', methods=['POST'])
def add_item_to_cart(cart_id: str):
    pass


@bp.route('/carts/<cart_id>/items', methods=['GET'])
def view_cart_items(cart_id: str):
    pass
