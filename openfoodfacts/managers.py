"""Create data from openfoofacts."""

from sqlalchemy.orm import sessionmaker

from . import engine
from .cleaner import DataCleaner
from .downloader import Downloader
from .models import Category, Product, Store


Session = sessionmaker(bind=engine)
session = Session()


class Manager:
    """ -tc- Base manager providing methods common to all managers."""

    def __init__(self, Model):
        """Intitalises the object attributes.

        Args:
            Model: Model used to build the reated instances

        """
        self.Model = Model

    def get_or_create(self, defaults=None, commit=True, **kwargs):
        """Looks up an object with the given kwargs, creating one if necessary."""
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
    """Store the data from the api in a MySQL database."""

    def save(self, stores):
        saved_stores = []
        for store_name in stores:
            saved_stores.append(
                self.get_or_create(store_name=store_name), commit=False
            )
        session.commit()
        return saved_stores


class CategoryManager:
    """Store the data from the api in a MySQL database."""

    def save(self, categories):
        saved_categories = []
        for store_name in categories:
            saved_categories.append(self.get_or_create(store_name=store_name))
        return saved_categories


class ProductManager:
    """Store the data from the api in a MySQL database."""

    pass

    def save(self):
        pass


if __name__ == "__main__":
    download = Downloader()
    cleaner = DataCleaner()

    storemanager = StoreManager(Store)

    products = download.get_product(1, 10)
    stores = cleaner.clean(products)
    storemanager.save(stores)

