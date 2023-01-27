from app import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    id: int
    name: str
    price: float
    description: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Numeric)
    description = db.Column(db.String(128))
