"""Create from openfoofacts."""

from cleaner import cleaner


class StoreManager:
    pass

    def save(self, stores):
        for store_name in stores:
            store = Store(store_name=store_name)
            session.add(store)
        session.commit()


class CategoryManager:
    pass

    def save(self):
        pass


class ProductManager:
    pass

    def save(self):
        pass
