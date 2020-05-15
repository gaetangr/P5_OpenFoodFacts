import requests

url = "https://fr.openfoodfacts.org/cgi/search.pl"

params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": 1,
            "json": 1,
            "page": 1
        }

response = requests.get(url, params=params)

data = response.json()

products = data["products"]
first_product = products[1]
code_product = first_product["code"]
name_product = first_product["product_name_fr"]
url_product = first_product["url"]
nutriscore_product = first_product["nutriscore_score"]
print(code_product, name_product, url_product, nutriscore_product)