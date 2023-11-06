from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    images = Column(String(200), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Desktop")
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()

        p1 = Product(name="Iphone 15 Pro", price=30000000, category_id=1)
        p2 = Product(name="Samsung Galaxy", price=25000000, category_id=1)
        p3 = Product(name="Oppo", price=15000000, category_id=1)
        p4 = Product(name="Realme", price=17000000, category_id=1)
        p5 = Product(name="Xiaome", price=12000000, category_id=1)
        p6 = Product(name="OnePlus", price=11000000, category_id=1)
        p7 = Product(name="Iphone 11 Promax", price=28000000, category_id=1)
        p8 = Product(name="Iphone XS Max", price=23000000, category_id=1)
        p9 = Product(name="Iphone 4 Plus", price=99999999, category_id=1)
        p10 = Product(name="Iphone 3 Plus", price=99999999, category_id=1)
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.add(p10)
        db.session.commit()