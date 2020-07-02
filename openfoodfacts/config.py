"""Config for the database and SqlAlchemy."""
import os

from dotenv import load_dotenv

############## DATABASE CONFIG ##############
load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE", "openfoodfacts")

############## REQUEST CONFIG ##############
