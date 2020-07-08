"""Display a menu for the user to choose a better product."""
from colorama import init
from colorama import Fore, Back, Style
init()
from .managers import session, Store, Category, Product
from pprint import pprint

class UserMenu:
    """Handle the logic to display the menu
    and fetch products from the database """
    def __init__(self):
        self.next = self.main_menu

    def start(self):
        self.running = True
        while self.running:
            self.next = self.next()

    def main_menu(self):
        """Display base menu for user """

        print(Fore.GREEN + "\n------ Menu principal ------\n")
        print(Fore.YELLOW + "1 - Choisir un substitut\n2 - Mes favoris")
        choice = input("Choissisez une option:")
        if choice == "1":
            print("hello")
        else:
            return getattr(self, choice)


    def category_menu(self):
        """Display categories for the user """

        print(Fore.GREEN + "\n------ Catégories ------\n")
        choice = input("Choissisez une catégorie:")
        return getattr(self, choice)

    def product_menu(self):
        """Display products once for a given category"""

        print(Fore.GREEN + "\n------ Produits ------\n")
        choice = input("Choissisez un produit:")
        return getattr(self, choice)

    def quit(self):
        """Quit the menu"""

        print("A bientôt")
        self.running = False    

        
if __name__ == "__main__":
    user_menu = UserMenu()
    user_menu.start()
    


        