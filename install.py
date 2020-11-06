"""Module responsible of creating and populating the database."""

from openfoodfacts.managers import productmanager, categorymanager, storemanager
from openfoodfacts.cleaner import DataCleaner
from openfoodfacts.downloader import Downloader


def main():
    """Main entry point of the installer."""
    print("Installation en cours...⏳")

    downloader = Downloader()
    cleaner = DataCleaner()

    products = downloader.get_product(100, 10)
    categories, products, stores = cleaner.clean(products)

    categorymanager.save(categories)
    storemanager.save(stores)
    productmanager.save(products)
    print(
        "Installation terminée ✅\nPour lancer le programme, veuillez utiliser la commande: python -m openfoodfacts"
    )


if __name__ == "__main__":
    main()