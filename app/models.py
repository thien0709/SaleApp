from importlib import import_module

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(200), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg')
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.username

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    product = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=True)
    image = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if (__name__ == "__main__"):
    with app.app_context():
        # pass
        db.create_all()
        c1 = Category(name = "Mobile")
        c2 = Category(name = "Tablet")
        c3 = Category(name = "PC")
        c4 = Category(name = "PCB")
        db.session.add_all([c1,c2,c3,c4])
        db.session.commit()
        import  json
        with open('data/products.json', encoding='utf-8') as f:
            product = json.load(f)
            for p in product:
                db.session.add(Product(**p))
        db.session.commit()
        import hashlib
        u = User(name = "Admin", username = "admin", password = "123")
        db.session.add(u)
        db.session.commit()