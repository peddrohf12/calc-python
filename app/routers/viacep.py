# app/routers/viacep.py
from fastapi import APIRouter, Depends, HTTPException
from ..auth import get_usuario_atual
from ..viacep import buscar_cep

router = APIRouter(prefix="/viacep", tags=["Via CEP"])

@router.get("/cep/{cep}")
def consultaCep(cep: str):
#def consultaCep(cep: str, usuario=Depends(get_usuario_atual)):
    return buscar_cep(cep)
