"""Config for the database and SqlAlchemy."""
import os

import mysql.connector
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
database = os.getenv("database")

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}', echo=True)
engine.execute("USE openfoodfacts")
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)
session = Session()
Base.metadata.create_all(engine)



