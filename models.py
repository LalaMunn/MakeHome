from sqlalchemy import  Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Web import db, app
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        #db.create_all()
        [{
            "id": 1,
            "name": "Mobile"
        }, {
            "id": 2,
            "name": "Tablet"
        }]

        products = [{
              "id": 1,
              "name": "iPhone 7 Plus",
              "description": "Apple, 32GB, RAM: 3GB, 10S13",
              "price": 17000000,
              "image": "images/p1.png",
              "category_id": 1
        }, {
              "id": 2,
              "name": "iPad Pro 2020",
              "description": "Apple, 128GB, RAM: 6GB",
              "price": 37000000,
              "image": "images/p2.png",
              "category_id": 2
        }, {
              "id": 3,
              "name": "Galaxy Note 10 Plus",
              "description": "Samsung, 64GB, RAM: 6GB",
              "price": 24000000,
              "image": "images/p3.png",
              "category_id": 1
        }, {
              "id": 4,
              "name": "Xiaomi Redmi Note 13 Pro+ 5G",
              "description": "Xiaomi, 256GB, RAM: 8GB",
              "price": 10990000,
              "image": "images/p5.png",
              "category_id": 1
        }]

        for p in products:
            pro = Product(name=p['name'], price=p['price'], image=p['image'], description=p['description'], category_id=p['category_id'])
            db.session.add(pro)

        db.session.commit()



