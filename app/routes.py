from app import app
from app.controllers import ProductController
from flask import request


@app.route('/api/product/csv', methods=['POST'])
def product_csv():
    return ProductController.create_from_csv(request.files['file'])


@app.route('/api/product', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProductController.all()
    else:
        return ProductController.create(request.get_json())


@app.route('/api/product/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product(product_id):
    if request.method == 'GET':
        return ProductController(product_id).get()
    elif request.method == 'PUT':
        return ProductController(product_id).update(request.get_json())
    elif request.method == 'DELETE':
        return ProductController(product_id).delete()
