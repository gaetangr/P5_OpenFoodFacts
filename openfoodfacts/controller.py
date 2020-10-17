"""Display a menu for the user to choose a better product."""
from colorama import init
from colorama import Fore, Back, Style

from .managers import session, Store, Category, Product
from pprint import pprint

init()

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
        """
        Display the main menu for the user in command line interface

        Returns:
            str: Return a list of choices 
        """

        print(Fore.GREEN + "\n------ Menu principal ------\n")
        print(Fore.YELLOW + "1 - Choisir un substitut\n2 - Mes favoris")
        choice = input("Choissisez une option:") #valider differents choix
        if choice == "1":
            print("hello") #return methode qui va bien, menu categorie, return self cateogry menu
            # def favoris menu
        else:
            return getattr(self, choice) # return self main menu on reaffiche le menu encore et encore


    def category_menu(self):
        """Display categories for the user

        Returns:
            str: Return a list of choices 
        """
        # afficher categories depuis base avec les chiffres jusqua 5
        print(Fore.GREEN + "\n------ Catégories ------\n")
        choice = input("Choissisez une catégorie:") # tant que pas de categorie continuer donc return categorie menu

        return getattr(self, choice)

    def product_menu(self):
        """Display products once for a given category
        
        Returns:
            str: Return a list of choices 
        """

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