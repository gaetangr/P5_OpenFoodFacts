"""Create data from openfoofacts."""

from sqlalchemy.orm import sessionmaker

from . import engine
from .cleaner import DataCleaner
from .downloader import Downloader
from .models import Category, Product, Store

Session = sessionmaker(bind=engine)
session = Session()


class Manager:
    """Base manager providing methods common to all managers."""

    def __init__(self, Model):
        """Intitalises the object attributes.

        Args:
            Model: Model used to build the reated instances
        """
        self.Model = Model

    def get_or_create(self, defaults=None, commit=True, **kwargs):
        """Looks up an object with the given kwargs, creating one if
        necessary."""
        if defaults is None:
            defaults = {}
        instance = session.query(self.Model).filter_by(**kwargs).first()
        if not instance:
            instance = self.Model(**kwargs, **defaults)
            session.add(instance)
            if commit:
                session.commit()
        return instance


class StoreManager(Manager):
    """Store the stores data from the api in a MySQL database."""

    def save(self, stores):
        saved_stores = []
        for store_name in stores:
            saved_stores.append(
                self.get_or_create(store_name=store_name), commit=False
            )
        session.commit()
        return saved_stores


class CategoryManager(Manager):
    """Store the categories data from the api in a MySQL database."""

    def save(self, categories):
        saved_categories = []
        for category_name in categories:
            saved_categories.append(
                self.get_or_create(category_name=category_name)
            )
        return saved_categories


class ProductManager(Manager):
    """Store the products data from the api in a MySQL database."""

    def save(self, products):

        for product_info in products:
            saved_products = products

            for category_name in saved_products['categories']:
                category = (
                    session.query(Category)
                    .filter_by(name=category_name)
                    .first()
                )
                product.categories.append(category)

            for store_name in product['stores']:
                store = session.query(Store).filter_by(name=store_name).first()
                product.stores.append(store)
        return saved_products
        


if __name__ == "__main__":
    download = Downloader()
    cleaner = DataCleaner()

    categorymanager = CategoryManager(Category)
    storemanager = StoreManager(Store)
    productmanager = ProductManager(Product)

    products = download.get_product(100, 10)

    categories, products, stores = cleaner.clean(products)

    productmanager.save(products)
    categorymanager.save(categories)
    storemanager.save(stores)
