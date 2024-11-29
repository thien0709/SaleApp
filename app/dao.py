import hashlib

from app import app
from app.models import Category, Product, User


def load_categories():
    return Category.query.order_by('id').all()


def load_products(kw=None, cate_id=None, page=1):
    query = Product.query
    if cate_id:
        query = query.filter(Product.category_id == cate_id)
    if kw:
        query = query.filter(Product.name.contains(kw))

    page_size = app.config['PAGE_SIZE']
    start = (int(page) - 1) * page_size
    query = query.slice(start, start + page_size)

    return query.all()

def count_products():
    return Product.query.count()

def auth_user(username, password):
    password = password
    return User.query.filter(User.name.__eq__(username), User.password.__eq__(password)).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)
