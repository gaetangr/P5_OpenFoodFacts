"""Display a menu for the user to choose a better product."""

class UserMenu:
    """Handle the logic to display the menu
    and fetch products from the database """
    def __init__(self):
        self.title = "\n---- OpenFoodFact Menu ----\n"
        self.user_choice = int(input("votre choix: "))
        self.substitute_choice = (
        f"{self.title}"
        "\nVeuillez faire un choix"
        "\n1. Sélectionnez par catégorie"
        "\n2. Sélectionnez par aliment"
        )
        self.menu_choice =  (
        f"{self.title}"
        "\nVeuillez faire un choix"
        "\n1. Quel aliment souhaitez-vous remplacer ?"
        "\n2. sa catégorie"
        )

    def main_menu(self):
        """Display the menu for the user"""
        running = True
        
        menu_choice = self.menu_choice

        substitute_choice = self.substitute_choice
        
        print(menu_choice)
        self.user_choice
        
        if self.user_choice == 1:
            print(substitute_choice)
                
            

    
            
        
        

if __name__ == "__main__":
    user_menu = UserMenu()
    user_menu.main_menu()
    