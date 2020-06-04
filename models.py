"""Create database and insert data from the API."""

from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = 'product'
    code_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    nutriscore_grade = Column(String)
    url = Column(String)

    def __repr__(self):
        """Render Product object in a readable way"""
        return f"{product_name} {nutriscore_grade} {url}"

class Store(Base):
    __tablename__ = 'store'
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String)

    def __repr__(self):
        """Render Store object in a readable way"""
        return f"{store_name}"


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    
    def __repr__(self):
        """Render Category object in a readable way"""
        return f"{category_name}"