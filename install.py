"""Module responsible of creating and populating the database."""

from openfoodfacts.managers import (
    productmanager, categorymanager, storemanager
)
from openfoodfacts.cleaner import DataCleaner
from openfoodfacts.downloader import Downloader


def main():
    """Main entry point of the installer."""
    downloader = Downloader()
    cleaner = DataCleaner()

    products = downloader.get_product(100, 10)
    categories, products, stores = cleaner.clean(products)

    categorymanager.save(categories)
    storemanager.save(stores)
    productmanager.save(products)


if __name__ == "__main__":
    main()