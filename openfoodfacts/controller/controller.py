"""Display a menu for the user to choose a better product."""

class UserMenu:
    """Handle the logic to display the menu
    and fetch products from the database """
    
    def __init__(self):
        self.title = "---- OpenFoodFacts Menu ----"
    
    def main_menu(self):
        """Display the menu for the user"""
        
        try:
            user_choice = int(input())     
        except ValueError as e:
            print("Merci de rentrer un choix entre 1 et 10")
            
            
        
        

if __name__ == "__main__":
    user_menu = UserMenu()
    user_menu.main_menu()