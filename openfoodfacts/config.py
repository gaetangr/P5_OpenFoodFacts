"""Config for the database and SqlAlchemy."""
import os

############## DATABASE CONFIG ##############

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE", "openfoodfacts")

#############################################

print(USER, PASSWORD, HOST, DATABASE)