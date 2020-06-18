"""Create from openfoofacts."""

from cleaner import cleaner


class StoreManager:
    """Store the data from the api in a MySQL database."""
    pass

    def save(self, stores):
        for store_name in stores:
            store = Store(store_name=store_name)
            session.add(store)
        session.commit()


class CategoryManager:
    """Store the data from the api in a MySQL database."""
    pass

    def save(self):
        pass


class ProductManager:
    """Store the data from the api in a MySQL database."""
    pass

    def save(self):
        pass
