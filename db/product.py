from db.basic_db import db_session
from db.models import Product

def save_products(items):
    db_session.add_all(items)
    db_session.commit()

def save_product(item):
    db_session.add_all(item)
    db_session.commit()