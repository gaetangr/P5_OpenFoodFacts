"""Create database and insert data from the API."""

from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = 'product'
    code_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    nutriscore_grade = Column(String)
    url = Column(String)


class Store(Base):
    __tablename__ = 'store'
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String)


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
