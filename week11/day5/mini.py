from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)


user_cart = []          #find way to do this without using globals (maybe OOP
total = 0


def import_data():
    with open("products.json") as file:
        data = json.load(file)
    return data

def find_item(product_id):
    data = import_data()
    for i, item in enumerate(data):
        if item['ProductId'] == product_id:
            product_index = i
    return data[product_index]


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/products')
def all_products():
    data = import_data()
    return render_template('products.html', data=data)


@app.route('/<ind_product>')
def single_product(ind_product):
    item = find_item(ind_product)
    return render_template('single_product.html', item=item)


@app.route('/cart')
def customer_cart():
    return render_template('user_cart.html', cart=user_cart, total=total)


@app.route('/addItem/<ProductId>')
def add_item(ProductId):
    global total
    item = find_item(ProductId)
    user_cart.append(item)
    total += item['Price']
    print(user_cart)
    return redirect(url_for('all_products'))


@app.route('/removeItem/<ProductId>')
def remove_item(ProductId):
    global total
    item = find_item(ProductId)
    user_cart.remove(item)
    total -= item['Price']
    print(user_cart)
    return redirect(url_for('customer_cart'))


if __name__ == "__main__":
    app.run(debug=True)
