"""Request data from OpenFoodFact and parse the result."""
from pprint import pprint

import requests


class Downloader:
    """Will download products from OpenFoodFacts/API."""

    def __init__(self):
        """Url : Takes the url from which the date is received
        Params : Takes parametres to filter the query"""
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": None,
            "json": 1,
            "page": 1,
            "fields": "nutriscore_grade,product_name,url,code,categories,stores",
        }

    def get_product(self, page_size=20, pages_number=1):
        """Display product based on specifics parameters."""
        params = self.params.copy()
        params["page_size"] = page_size
        products = []
        try:
            response = requests.get(self.url, params=params, timeout=2)
            data = response.json()
        except requests.exceptions.ReadTimeout:
            print("Error when fetching the API")
        for i in range(pages_number):
            params["page"] = i + 1
            response = requests.get(self.url, params=params)
            if response.status_code == 200:
                products.extend(response.json()["products"])
        return products


class DataCleaner:
    """Will clean the data received from the API."""

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
        return clean_products


if __name__ == "__main__":
    download = Downloader()
    cleaner = DataCleaner()
    products = download.get_product(1, 1200)
    print(len(products))
