from app.models import Category, Product, User


def get_categories():
    return Category.query.all()


def get_products(kw):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))
    return products.all();


def get_user_by_id(user_id):
    return User.query.get(user_id)