from app.models import Category, Product


def load_categories():
    return Category.query.order_by('id').all()


def load_products(kw=None, cate_id=None):
    query = Product.query
    if cate_id:
        query = query.filter(Product.category_id == cate_id)
    if kw:
        query = query.filter(Product.name.contains(kw))
    return query.all()
