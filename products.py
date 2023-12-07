products = [
    {'id': 1, 'name': 'Product 1', 'price': 20.0},
    {'id': 2, 'name': 'Product 2', 'price': 30.0},
    {'id': 3, 'name': 'Product 3', 'price': 25.0},
]

def get_all_products():
    return products

def get_product_by_id(product_id):
    return next((product for product in products if product['id'] == product_id), None)
