"""Create from openfoofacts."""

from sqlalchemy.orm import sessionmaker

from .cleaner import DataCleaner
from .downloader import Downloader
from .models import Category, Product, Store
from openfoodfacts import engine


Session = sessionmaker(bind=engine)
session = Session()

class StoreManager:
    """Store the data from the api in a MySQL database."""

    def save(self, stores):
        for store_name in stores:
            store = Store(store_name=store_name)
            session.add(store)
        session.commit()


class CategoryManager:
    """Store the data from the api in a MySQL database."""

    def save(self):
        for store_name in stores:
            store = Store(store_name=store_name)
            session.add(store)
        session.commit()


class ProductManager:
    """Store the data from the api in a MySQL database."""

    pass

    def save(self):
        pass


if __name__ == "__main__":
    download = Downloader()
    cleaner = DataCleaner()
    storemanager = StoreManager()

    products = download.get_product(1, 10)
    stores = cleaner.clean(products)
    save = storemanager.save(stores)
    print(save)


