"""Config for the database and SqlAlchemy."""
import os


############## DATABASE CONFIG ##############

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE", "openfoodfacts")

############## DISPLAY CONFIG ##################

# Changing this value with increase or decrease the number of data being display on the screen..
# ..the bigger the number the slower the program
display_limit = 6
