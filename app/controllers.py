import pandas as pd
from app import db
from app.models import Product
from flask import jsonify


class ProductController:

    def __init__(self, product_id):
        self.product_id = product_id

    @staticmethod
    def create_from_csv(csv):
        df = pd.read_csv(csv)
        df.to_sql('product', db.engine, 'dafitiapi', if_exists='append', index=False)
        return jsonify({'status': 'ok'}), 200

    @staticmethod
    def create(product):
        name, price = product.get('name'), product.get('price')
        if name and price and (type(price) == float or type(price) == int):
            new_product = Product(name=name, price=price, description=product.get('description'))
            db.session.add(new_product)
            db.session.commit()
            return jsonify({'status': 'ok'}), 200
        return jsonify({'status': 'error'}), 400

    @staticmethod
    def all():
        return jsonify({'status': 'ok', 'response': Product.query.all()}), 200

    def get(self):
        product = Product.query.get(self.product_id)
        if product:
            return jsonify({'status': 'ok', 'response': product}), 200
        return jsonify({'status': 'not found'}), 404

    def update(self, updates):
        product = Product.query.get(self.product_id)
        if product and updates:
            Product.query.filter_by(id=self.product_id).update(updates)
            db.session.commit()
            return jsonify({'status': 'ok'}), 200
        return jsonify({'status': 'error'}), 400

    def delete(self):
        product = Product.query.get(self.product_id)
        if product:
            product.delete()
            db.session.commit()
            return jsonify({'status': 'ok'}), 200
        return jsonify({'status': 'not found'}), 404
