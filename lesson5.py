from flask import *

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('shoppinglist.html')


@app.route('/showitems', methods=['POST'])
def show_items():
    product = request.form['product']
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    price = request.form['price']
    return render_template('showitems.html', product=product, product_id=product_id, quantity=quantity, price=price)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5050)