from sqlalchemy import create_engine
from.config import USER, PASSWORD, HOST, DATABASE

engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4', echo=True)


