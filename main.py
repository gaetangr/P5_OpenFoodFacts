#! /usr/bin/env python3
"""Request data from OpenFoodFact and parse the result"""

import requests
import json
  
class downloader:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.number_products = 10
        self.params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": 1,
            "json": 1,
            "page": 1
        }
        self.response = requests.get(self.url, params=self.params)
        self.data = self.response.json()
    
    def display_products(self):
        
        product = self.data["products"]
        id_product = 0
        for field in range(self.number_products):
            products_list = product[id_product]
            code_product = products_list["code"]
            name_product = products_list["product_name_fr"]
            url_product = products_list["url"]
            nutriscore_product = products_list["nutriscore_score"]
            print(f"Code {code_product} - {name_product} {url_product} - Nutriscore {nutriscore_product}")
            id_product += 1
    
download = downloader()
download.display_products()
