"""Create data from openfoofacts."""

from pprint import pprint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from . import engine
from .models import Category, Product, Store, Favorite
from .config import display_limit

Session = sessionmaker(bind=engine)
session = Session()


class Manager:
    """Base manager providing methods common to all managers."""

    def __init__(self, Model):
        """Intitalises the object attributes.

        Args:
            Model: Model used to build the created instances
        """
        self.Model = Model

    def get_or_create(self, defaults=None, commit=True, **kwargs):
        """Looks up an object with the given kwargs, creating one if
        necessary.

        Args:
            defaults ([type], optional): [description]. Defaults to None.
            commit (bool, optional): [description]. Defaults to True.

        Returns:
            [type]: [description]
        """
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
            saved_stores.append(self.get_or_create(store_name=store_name, commit=False))
        session.commit()
        return saved_stores


class CategoryManager(Manager):
    """Store the categories data from the api in a MySQL database."""

    def save(self, categories):
        """Method to save the categories inside my database

        Args:
            categories (list): Products categories from the API

        Returns:
            list: return a list of categories
        """
        saved_categories = []
        for category_name in categories:
            saved_categories.append(
                self.get_or_create(category_name=category_name, commit=False)
            )
        session.commit()
        return saved_categories

    def get_categories_randomly(self):
        """Return a given number of categories chosen randomly."""
        return session.query(Category).limit(display_limit).all()


class ProductManager(Manager):
    """Store the products data from the api in a MySQL database."""

    def save(self, products):
        """Save the products data from the api in a MySQL database.

        Args:
            products (list): Products from the API

        Returns:
            list: return a list of products
        """
        saved_products = []
        for product_info in products:
            product = self.get_or_create(
                id=int(product_info.get("code")),
                defaults={
                    "product_name": product_info.get("product_name"),
                    "nutriscore_grade": product_info.get("nutriscore_grade"),
                    "url": product_info.get("url"),
                },
            )
            saved_products.append(product)
            for category_name in product_info["categories"]:
                category = (
                    session.query(Category)
                    .filter_by(category_name=category_name)
                    .first()
                )
                product.categories.append(category)

            for store_name in product_info["stores"]:
                store = session.query(Store).filter_by(store_name=store_name).first()
                product.stores.append(store)

            session.add(product)
        session.commit()
        return saved_products


class FavoriteManager(Manager):
    """Store the favorite data from the api in a MySQL database."""

    def get_products(self):
        """Return product save from data"""
        return session.query(Favorite).all()

    def save_favorite(self, product_fav):
        """Save given product into favorite menu

        Args:
            product_fav (string): favorite product
            to be saved into the database
        """
        favorite_data = Favorite(product_sub=product_fav)
        session.add(favorite_data)
        session.commit()


# Create managers as singletons
categorymanager = CategoryManager(Category)
storemanager = StoreManager(Store)
productmanager = ProductManager(Product)
favoritemanager = FavoriteManager(Favorite)
