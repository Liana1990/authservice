from database import Base
from sqlalchemy import Column,Integer, String, TIMESTAMP, text,Date


class User (Base):
    __tablename__= "users"
    id = Column(Integer, nullable=False, primary_key=True)

    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    gender= Column(String(1), nullable=True)
    birthdate=Column(Date, nullable=True)
    imagename=Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Code(Base):
    __tablename__ = "code"
    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String(128), nullable=False)
    code = Column(String(6), nullable=False,unique=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


