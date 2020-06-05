from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Session = sessionmaker()
session = Session()
Base = declarative_base()
Base.metadata.create_all(engine)


class Product(Base):
    __tablename__ = 'product'
    code_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    nutriscore_grade = Column(String)
    url = Column(String)

    def __repr__git(self):
        """Render Product object in a readable way."""
        return f"{product_name} {nutriscore_grade} {url}"


class Store(Base):
    __tablename__ = 'store'
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String(80), unique=True)

    def __repr__git(self):
        """Render Store object in a readable way."""
        return f"{store_name}"


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(100), unique=True)

    def __repr__git(self):
        """Render Category object in a readable way."""
        return f"{category_name}"


Session.configure(bind=engine)
test_cat = Category(category_name='Jus de fruits')
session.add(test_cat)
session.commit()
