import os

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_BASE_URL = os.environ.get("API_BASE_URL")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        product_data = {
            'name': request.form['name'],
            'price': request.form['price'],
            'description': request.form['description']
        }
        requests.post(f'{API_BASE_URL}/products/', json=product_data)
        return redirect(url_for('index'))
    return render_template('create_product.html')


@app.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    if request.method == 'POST':
        product_data = {
            'name': request.form['name'],
            'price': request.form['price'],
            'description': request.form['description']
        }
        requests.put(f'{API_BASE_URL}/products/{product_id}/', json=product_data)
        return redirect(url_for('index'))

    response = requests.get(f'{API_BASE_URL}/products/{product_id}/')
    product = response.json()
    return render_template('update_product.html', product=product)


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    requests.delete(f'{API_BASE_URL}/products/{product_id}/')
    return redirect(url_for('index'))


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user_data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': request.form['password']
        }
        requests.post(f'{API_BASE_URL}/users/', json=user_data)
        return redirect(url_for('index'))
    return render_template('create_user.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)