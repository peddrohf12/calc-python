# app/models.py
from pydantic import BaseModel

class OperacaoDoisNumeros(BaseModel):
    a:float
    b:float

class OperacaoRaiz(BaseModel):
    numero:float
    indice:float = 2