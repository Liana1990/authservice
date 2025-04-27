from auth import users_auth_router
from fastapi import FastAPI
from models import Base
from database import engine # databazayin kpnelu hamar

Base.metadata.create_all(bind=engine)# table sarqelu hamar
app=FastAPI() #himnakan app

import psycopg2 # connection u cursor anelu hamar
from psycopg2.extras import RealDictCursor#databasayic tvyalner@ dictiponariov gan

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='authserverdb',
    user='postgres',
    password='liana1990',
    cursor_factory=RealDictCursor
) #databasayi mej tvyalner@ grelu hamar
cursor = conn.cursor()
@app.get("/")
def main():
    return "ok"

app.include_router(users_auth_router)# auth filei meji apiner@ kpnen himnakan appin u documentaciayi mej ereva