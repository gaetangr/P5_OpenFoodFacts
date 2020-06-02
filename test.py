class DataCleaner:
    """Will clean the data received from the API"""

    def is_valid(self, product): 
        if product.get("nutriscore_grade") and product.get("product_name") and product.get("url") and product.get("code") and product.get("categories") and product.get("stores"): 
            return True
  
    def clean(self, products): #boucle for et appeler is valid
        clean_products = [2]
   

classe = DataCleaner()
classe.clean_products