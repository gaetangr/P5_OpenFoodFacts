"""Display a menu for the user to choose a better product."""
from colorama import init
from colorama import Fore, Back, Style

from .managers import session, Store, Category, Product
from pprint import pprint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func, select

from . import engine

Session = sessionmaker(bind=engine)
session = Session()

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
        choice = input("Choissisez une option:")
        if choice == "1":
            return self.category_menu
        elif choice == "2":
            return self.favorite_menu
        else:
            print("Choix invalide")
            return self.main_menu

    def favorite_menu(self):
            """Display favoris for the user

            Returns:
                str: Return a list of choices 
            """
            # afficher categories depuis base avec les chiffres jusqua 5
            print(Fore.GREEN + "\n------ Favoris ------\n")
            choice = input("Choissisez une option:")
            return self.main_menu
            

    def category_menu(self):
        """Display categories for the user

        Returns:
            str: Return a list of choices 
        """
        q = session.query(Category.category_name).order_by(func.random()).limit(6).all()
        print(Fore.GREEN + "\n------ Catégories ------\n")
        for n, category_name in enumerate(q):
            print(f"{n} - {category_name}")
        choice = input("Choissisez une option:")
        return self.main_menu
    

    def product_menu(self):
        """Display products once for a given category
        
        Returns:
            str: Return a list of choices 
        """
        q = session.query(Product.product_name).order_by(func.random()).limit(6).all()
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
