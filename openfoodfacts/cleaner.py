"""Module to cleaned and normalize data from downloader module."""

class DataCleaner:
    """Clean the data received from the API."""

    def is_valid(self, product):
        if (
            product.get("nutriscore_grade")
            and product.get("product_name")
            and product.get("url")
            and product.get("code")
            and product.get("categories")
            and product.get("stores")
        ):
            return True

    def clean(self, products):
        """Parse and normalize data from the API."""
        clean_products = []
        clean_stores = set()
        clean_categories = set()
        for product in products:
            if self.is_valid(product):
                product["categories"] = [
                    cat.strip().lower().capitalize()
                    for cat in product["categories"].split(",")
                ]
                product["stores"] = [
                    store.strip().lower().capitalize()
                    for store in product["stores"].split(",")
                ]
                clean_products.append(product)
                clean_stores |= set(product["stores"])
                clean_categories |= set(product["categories"])
        return clean_categories, clean_products, clean_stores