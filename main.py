#! /usr/bin/env python3
"""Request data from OpenFoodFact and parse the result."""
from pprint import pprint
import json

import requests

# stores / unique_scans_n / url / product_name / nutriscore_grade / categories

class Downloader:
    """Will download products from OpenFoodFacts"""

    def __init__(self):
        """[summary]"""
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": 40, 
            "json": 1,
            "page": 5,
        }
        

    def get_product(self):
        """Display product based on specifics params."""
        response = requests.get(self.url, params=self.params)
        data = response.json()
        products = data["products"]
        products_list = []
        pprint(products_list)
        
        for product in products:
            #code_product = product["unique_scans_n"]
            name_product = product["product_name"]
            # url_product = product["url"]
            # nutriscore_product = product["nutriscore_grade"]
            # store = product["url"]
            #pprint(f" {store}")
            products_list.append(name_product)
            
        pprint(products_list)
        cleaned = [x.lower().capitalize() for x in products_list]
        pprint(cleaned)

class DataCleaner:

    def is_valid(self, product):
        pass 

    def clean(self, products):
        clean_products = []
        if products[7]["origins"]  :
            print(True)
            clean_products.append(data)
        else:
            print(False)
        return products


download = Downloader()
products = download.get_product()



