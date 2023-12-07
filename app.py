from flask import Flask, render_template, request, redirect, url_for, session
from products import get_all_products

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    product = get_product_by_id(product_id)
    session['cart'].append(product)

    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    if 'cart' not in session:
        session['cart'] = []

    total = sum(product['price'] for product in session['cart'])
    return render_template('cart.html', cart=session['cart'], total=total)

if __name__ == '__main__':
    app.run(debug=True)
