"""Module responsible of creating and populating the database."""

from openfoodfacts import managers
from openfoodfacts.cleaner import DataCleaner
from openfoodfacts.downloader import Downloader


def main():
    """Main entry point of the installer."""
    downloader = Downloader()
    cleaner = DataCleaner()

    products = downloader.get_product(100, 10)
    categories, products, stores = cleaner.clean(products)

    managers.categorymanager.save(categories)
    managers.storemanager.save(stores)
    managers.productmanager.save(products)


if __name__ == "__main__":
    main()