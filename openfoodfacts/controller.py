"""Display a menu for the user to choose a better product."""
import time

from colorama import Fore, init
from sqlalchemy.orm import sessionmaker

from . import engine
from .config import display_limit
from .managers import Category, Product, Store, session
from .managers import categorymanager, favoritemanager

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
        """Initialize the menu"""
        self.next = self.main_menu

    def start(self):
        """Keep the menu running"""
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
        favorite = favoritemanager.get_products()
        print(Fore.GREEN + "\n------⭐ Favoris ⭐------\n")
        for favorite_product in favorite:
            print(favorite_product)
        choice = input("\nChoissisez une option:")
        return self.main_menu

    def favorite_details_menu(self):
        pass

    def category_menu(self):
        """Display categories for the user

        Returns:
            str: Return a list of choices
        """
        category = categorymanager.get_categories_randomly()

        print(Fore.GREEN + "\n------🍩 Catégories 🍩------\n")
        for n, category_n in enumerate(category):
            if len(category_n.category_name) >= 31:
                truncate = f"{category_n.category_name[:30]} (...)"
            else:
                truncate = category_n.category_name

            content = f"{n} - {truncate} | ({len(category_n.products)})"
            if len(category_n.products) > 1:
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
            try:
                choice = int(choice)
                self.category = category[choice]
                return self.product_menu
            except IndexError as e:
                print(
                    Fore.RED + "⛔️ Vous avez choisi un numéro hors index",
                    "- Erreur:",
                    e,
                )
                return self.category_menu

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
            return self.category_menu
        else:
            choice = int(choice)

            print(f"Vous avez choisi: {self.category.products[choice]}\n")
        if self.category.products[choice].nutriscore_grade in good_products:
            print(
                "🤷‍ Nous n'avons trouvé aucun substitue, il est peut-être trop bon...\n Retour au menu principal"
            )
            return self.main_menu

        elif self.category.products[choice].nutriscore_grade in bad_products:
            for n, product_n.nutriscore_grade in enumerate(good_products):
                print(Fore.GREEN + "Nous vous proposons:\n")
                print(f"🍽  {product_n} - 🔗 URL: {product_n.url}")
                print(
                    f"\n👉Vous pouvez l'acheter aux magasins suivants: {product_n.stores}\n"
                )
                choice = input(
                    Fore.YELLOW
                    + "Voulez-vous enregistrer le substitue ?\n1 - Enregistrer ⭐\n2 - Quitter ❌"
                )

                if not choice.isdigit():
                    print(Fore.RED + "\n ⚠ Choix invalide ⚠")
                    return self.product_menu
                elif choice == "1":
                    choice = int(choice)
                    product_fav = str(f"{product_n} - 🔗 URL: {product_n.url}")
                    favoritemanager.save_favorite(product_fav)
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
