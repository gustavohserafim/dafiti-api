import random
import requests
from faker import Faker
import csv


class Tests:

    def __init__(self):
        self.url = "http://localhost:5000/api/product"
        self.create_products_csv()
        self.get_products_csv()
        self.get_all_products()
        self.get_one_product()
        self.update_product()
        self.delete_product()
        self.create_and_get_csv_product()
        self.get_csv_min_price()
        self.get_csv_max_price()
        self.get_csv_all_params()

    # Gera um CSV com produtos e faz requisição para criação em lote
    def create_products_csv(self):
        fake = Faker()
        with open('tests/generated_products.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(1, 2001):
                writer.writerow({'name': 'Produto ' + str(_), 'price': fake.random_number(digits=4),
                                 'description': 'Descricao do produto ' + str(_)})

        file = {'file': open('tests\generated_products.csv', 'rb')}
        r = requests.post(self.url + "/csv", files=file)
        assert r.status_code == 200

    # Gera CSV com todos produtos
    def get_products_csv(self):
        r = requests.get(self.url + "/csv")
        open('tests\downloaded_products.csv', 'wb').write(r.content)
        assert r.status_code == 200

    # CRUD, read all
    def get_all_products(self):
        r = requests.get(self.url)
        assert r.status_code == 200

    # CRUD, read
    def get_one_product(self):
        r = requests.get(self.url + "/1")
        assert r.status_code == 200

    # CRUD, update
    def update_product(self):
        old_product = requests.get(self.url + "/1").json()['response']
        requests.put(self.url + "/1", json={'name': "tested Produto 1 alterado " + str(random.randint(1, 9999)),
                                            'description': 'descricao alterada' + str(random.randint(1, 9999)),
                                            'price': 1001})
        updated_product = requests.get(self.url + "/1").json()['response']
        assert old_product.get('name') != updated_product.get('name') and old_product.get(
            'description') != updated_product.get('description')

    # CRUD, delete
    def delete_product(self):
        requests.delete(self.url + "/2")
        r = requests.get(self.url + "/2")
        assert r.status_code == 404

    # Cria um produto e faz o download do CSV passando o parametro
    def create_and_get_csv_product(self):
        r = requests.post(self.url, json={'name': 'tested product', 'price': 999, 'description': 'created by test'})
        created_product = requests.get(self.url + '/csv?name=tested')
        open('tests\created_product.csv', 'wb').write(created_product.content)
        assert r.status_code == 200

    # Download do csv personalizado com o parametro de min_price
    def get_csv_min_price(self):
        r = requests.get(self.url + '/csv?min_price=5000')
        open('tests\min_price_products.csv', 'wb').write(r.content)
        assert r.status_code == 200

    # Download do csv personalizado com o parametro de max_price
    def get_csv_max_price(self):
        r = requests.get(self.url + '/csv?max_price=5000')
        open('tests\max_price_products.csv', 'wb').write(r.content)
        assert r.status_code == 200

    # Download do csv personalizado com todos os parametros
    def get_csv_all_params(self):
        r = requests.get(self.url + '/csv?name=tested&min_price=999&max_price=1001')
        open('tests\params_products.csv', 'wb').write(r.content)
        assert r.status_code == 200


if __name__ == '__main__':
    Tests()
