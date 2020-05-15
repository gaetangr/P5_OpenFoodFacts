import requests
import json
  
class downloader:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.page_size = 1
        self.params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": self.page_size,
            "json": 1,
            "page": 1
        }
        self.response = requests.get(self.url, params=self.params)
        self.data = self.response.json()
    
    def display_request(self):
        product = self.data["products"]
        first_product = product[0]
        for field in first_product:
            print(len(field))
    
download = downloader()
download.display_request()


"""
url, code, nutriscore
1 - product downloader classe avec params
2 - download de la liste de produits, 10 000 produits / 100 de produits
3 - autre classe cleaning, en entrée liste 100 produits if no data on l'eleve produit
4- classe enregistrment donne product manager dans bdd
"""