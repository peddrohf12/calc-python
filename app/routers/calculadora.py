# app/routers/calculadora.py

from fastapi import APIRouter, Depends, HTTPException
from ..models import OperacaoDoisNumeros, OperacaoRaiz
import math
from ..auth import get_usuario_atual

router = APIRouter(prefix="/calc", tags=["Calculadora"])

@router.get("/somar")
def somar(a:float, b:float, usuario=Depends(get_usuario_atual)):
    """
    Destinado para execução da soma em modo GET
    """
    return {"resultado": a+b} 

@router.post("/subtrair")
def subtrair(dados: OperacaoDoisNumeros, usuario=Depends(get_usuario_atual)):
    return {"resultado": dados.a - dados.b}

@router.post("/multiplicar")
def multiplicar(dados: OperacaoDoisNumeros, usuario=Depends(get_usuario_atual)):
    return {"resultado": dados.a * dados.b}

@router.post("/dividir")
def dividir(dados: OperacaoDoisNumeros, usuario=Depends(get_usuario_atual)):
    if dados.b == 0:
        raise HTTPException(status_code=400, detail="Não é permitido dividir por zero")
    return {"resultado": dados.a / dados.b}

@router.post("/potencia")
def potencia(dados: OperacaoDoisNumeros, usuario=Depends(get_usuario_atual)):
    #return {"resultado": math.pow(dados.a, dados.b)}
    return {"resultado": dados.a ** dados.b}

@router.post("/raiz")
def raiz(dados: OperacaoRaiz, usuario=Depends(get_usuario_atual)):
    if dados.indice == 0:
        raise HTTPException(status_code=400, detail="Não é permitido indice zero")
    return {"resultado": dados.numero ** (1/dados.indice)}
