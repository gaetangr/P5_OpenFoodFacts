"""Display a menu for the user to choose a better product."""
import time
from pprint import pprint

from colorama import Back, Fore, Style, init
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func, select

from . import engine
from .config import display_limit
from .managers import Category, Product, Store, session

Session = sessionmaker(bind=engine)
session = Session()

init()


class UserMenu:
    """
    This class take care of the whole
    menu logic where each methods handle
    a different menu allowing a very
    flexible navigation between them
    """

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
        print(
            Fore.YELLOW + "1 - Choisir un substitut 🍩\n2 - Mes favoris ⭐\n3 - Quitter ❌"
        )
        choice = input("\nChoissisez une option:")
        if choice == "1":
            return self.category_menu
        elif choice == "2":
            return self.favorite_menu
        elif choice == "3":
            return self.quit
        else:
            print(Fore.RED + "\n ⚠ Choix invalide ⚠")
            return self.main_menu

    def favorite_menu(self):
        """Display favoris for the user

        Returns:
            str: Return a list of choices
        """
        print(Fore.GREEN + "\n------⭐ Favoris ⭐------\n")
        choice = input("\nChoissisez une option:")
        return self.main_menu

    def category_menu(self):
        """Display categories for the user

        Returns:
            str: Return a list of choices
        """
        category = (
            session.query(Category).order_by(func.random()).limit(display_limit).all()
        )

        print(Fore.GREEN + "\n------🍩 Catégories 🍩------\n")
        for n, category_n in enumerate(category):
            if len(category_n.category_name) >= 31: # Truncate products if too long
                truncate = f"{category_n.category_name[:30]} (...)"
            else:
                truncate = category_n.category_name

            content = f"{n} - {truncate} | ({len(category_n.products)})"
            if len(category_n.products) > 1: # plural if more than one product in DB
                print(f"{content} produits")
            else:
                print(f"{content} produit")

        print(
            Fore.YELLOW
            + "\nAstuce: Appuyez sur <entrée> pour afficher de nouvelles catégories"
        )
        choice = input("\nChoissisez une catégorie:")
        print()
        if not choice.isdigit():
            print(Fore.RED + "\n ⚠ Choix invalide ⚠")
            return self.category_menu
        else:
            choice = int(choice)
            self.category = category[choice]
            return self.product_menu

    def product_menu(self):
        """Display products once for a given category

        Returns:
            str: Return a list of choices
        """
        good_products = ["a", "b"]
        bad_products = ["c", "d", "e", "f"]

        for n, product_n in enumerate(self.category.products):
            content = f"{n} - {product_n} | Nutriscore: [{product_n.nutriscore_grade.upper()}]"
            if product_n.nutriscore_grade in good_products:
                rating = print(f"{content} | 👍")
            elif product_n.nutriscore_grade in bad_products:
                rating = print(f"{content} | 👎") 

        choice = input("\nChoissisez un produit à substituer:")
        if not choice.isdigit():
            print(Fore.RED + "\n ⚠ Choix invalide ⚠")
            return self.product_menu
        else:
            choice = int(choice)
            print(f"Vous avez choisi: {self.category.products[choice]}\n")
            for n, product_n in enumerate(self.category.products):
                if product_n.nutriscore_grade in good_products:
                    print(Fore.GREEN + "Nous vous proposons:\n")
                    print(f"🍽 {product_n} - 🔗 URL: {product_n.url}")
                    print(f"Vous pouvez l'acheter aux magasins suivants: {product_n.stores}\n")
                    choice = input(Fore.YELLOW + "Voulez-vous enregistrer le substitue ?\n1 - Enregistrer ⭐\n2 - Quitter ❌")
                    choice = int(choice)
                    if not choice.isdigit():
                        print(Fore.RED + "\n ⚠ Choix invalide ⚠")
                        return self.product_menu
                    elif choice == "1":
                        return self.favorite_menu()
                    elif choice == "2":
                        return self.main_menu
                

    def quit(self):
        """Quit the menu and wave goodbye"""

        choice = input(Fore.RED + "Voulez-vous quitter le programme [O/N] ?")
        if choice == "O" or "o":
            print(Fore.RED + "Merci d'avoir utilisé le programme 👋 ")
            time.sleep(2)
            self.running = False
        else:
            return self.category_menu


if __name__ == "__main__":

    user_menu = UserMenu()
    user_menu.start()
