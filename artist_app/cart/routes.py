from artist_app.cart import bp

@bp.route('/carts', methods=['POST'])
def create_cart():
    pass


@bp.route('/carts/<cart_id>', methods=['GET'])
def get_cart(cart_id: str):
    pass


@bp.route('/carts/<cart_id>/items', methods=['POST'])
def add_item_to_cart(cart_id: str):
    pass


@bp.route('/carts/<cart_id>/items', methods=['GET'])
def view_cart_items(cart_id: str):
    pass
