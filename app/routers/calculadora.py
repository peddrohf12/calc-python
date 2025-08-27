# app/routers/calculadora.py

from fastapi import APIRouter, HTTPException
from ..models import OperacaoDoisNumeros, OperacaoRaiz
import math

router = APIRouter(prefix="/calc", tags=["Calculadora"])

@router.get("/somar")
def somar(a:float, b:float):
    return {"resultado": a+b} 

@router.post("/subtrair")
def subtrair(dados: OperacaoDoisNumeros):
    return {"resultado": dados.a - dados.b}

@router.post("/multiplicar")
def multiplicar(dados: OperacaoDoisNumeros):
    return {"resultado": dados.a * dados.b}

@router.post("/dividir")
def dividir(dados: OperacaoDoisNumeros):
    if dados.b == 0:
        raise HTTPException(status_code=400, detail="Não é permitido dividir por zero")
    return {"resultado": dados.a / dados.b}

@router.post("/potencia")
def potencia(dados: OperacaoDoisNumeros):
    #return {"resultado": math.pow(dados.a, dados.b)}
    return {"resultado": dados.a ** dados.b}

@router.post("/raiz")
def raiz(dados: OperacaoRaiz):
    if dados.indice == 0:
        raise HTTPException(status_code=400, detail="Não é permitido indice zero")
    return {"resultado": dados.numero ** (1/dados.indice)}
