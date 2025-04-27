from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:liana1990@localhost:5432/authserverdb"
# table ner@ chish texu sarqelu hamar e
engine = create_engine(SQLALCHEMY_DATABASE_URL)# tablener@ gnan chisht texum sarqven
Base = declarative_base() #modelner@ jarangven Basic ev da ditvi vorpes sqli databasayi table
