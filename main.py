'''
    Micro servicio hecho con python y de framework FastAPI
    Para poder ejecutarlo primeramente tenemos que ambientarlo asi:
    1. Primeramente tenemos que crear un entorno virtual usando una temrinal:
        python -m venv fastapi-env
    2. Si no nos arroja error, activamos nuestro entorno virtual de la siguiente manera:
        fastapi-env\Script\activate.bat
    3. Realizar las instalaciones necesarias para trabajar con FastAPI
        a) pip install fastapi
        b) pip install uvicorn
    4. Vamos a VSCode y programamos el codigo de nuestro archivo main.py (ya hecho)
    5. Una vez terminados los endpoints ejecutamos el siguiente comando en la terminal:
        uvicorn main:app --reload
'''

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial:Optional[str]


@app.get("/saluda")
def index():
    return {"message":"Hola Pythonianos!"}


@app.get("/libros/{id}")
def mostrarLibro(id:int):
    if id%2==0:
        return {"data":id, "nombre":"Libro Par"}
    else:
        return {"data":id, "nombre":"Libro Impar"}


@app.post("/libros")
def insertarLibro(libro:Libro):
    return {"mesage":f"Libro '{libro.titulo}' ha sido insertado!"}
