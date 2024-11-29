from flask_admin import  Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from app.models import Category, Product

admin = Admin(app, name='Sale App', template_mode='bootstrap4')

class MyCategoryView(ModelView):
    column_list = ['name', 'product']
    column_searchable_list = ['id','name']

class MyProductView(ModelView):
    column_searchable_list = ['id','name']
    column_filters = ['id','name']

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
