from fastapi import FastAPI
from typing import Optional
import uvicorn
from db import engine,connection_db,conn
from sqlalchemy import func, select

app = FastAPI()


from models import *
@app.get('/hello')
def hello():
    return {"respuesta":'hola'}

@app.get('/datos_faker')
def datos():
    a = conn.execute(datos_falsos.select()).fetchall()
    return {"respuesta":a}

@app.get('/insert_data')
def insert_data():
    new_data = {"name": "pacho", "email": "pacho@gmail.com"}
    result = conn.execute(datos_falsos.insert().values(new_data))
    return {"respuesta":"asdasdasd"}
