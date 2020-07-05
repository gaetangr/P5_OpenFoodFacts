from sqlalchemy import create_engine

from .config import DATABASE, HOST, PASSWORD, USER

engine = create_engine(
    f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}', echo=True
)
