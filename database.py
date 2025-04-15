from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:liana1990@localhost:5432/authserverdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
