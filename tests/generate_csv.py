from faker import Faker
import csv

fake = Faker()

# Cria o arquivo CSV
with open('tests/generated_products.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'price', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(1, 2001):
        writer.writerow({'name': 'Produto ' + str(_), 'price': fake.random_number(digits=4), 'description': 'Descricao do produto ' + str(_)})
