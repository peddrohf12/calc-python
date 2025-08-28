# app/routers/usuarios.py
from fastapi import APIRouter, HTTPException
from ..models import UsuarioLogin
from ..auth import get_usuario, gerar_hash

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/test")
def test():
    return {"mensagem": "OK, tudo certo!"}

@router.post("/registro")
def registrar(usuario: UsuarioLogin):
    if get_usuario(usuario.username):
        raise HTTPException(status_code=400, detail='Usuário já existe')

    hash_senha = gerar_hash(usuario.password)

    return {"mensagem": "OK!" , "hash" : hash_senha} 