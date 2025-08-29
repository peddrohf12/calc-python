# app/routers/usuarios.py
from fastapi import APIRouter, HTTPException
from ..models import UsuarioLogin
from ..auth import get_usuario, gerar_hash, autenticar_usuario, criar_token
from ..database import usuarios
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/test")
def test():
    return {"mensagem": "OK, tudo certo!"}

@router.post("/registro")
def registrar(usuario: UsuarioLogin):
    if get_usuario(usuario.username):
        raise HTTPException(status_code=400, detail='Usuário já existe')
    hash_senha = gerar_hash(usuario.password)
    usuarios.insert_one({"username":usuario.username, "password": hash_senha})
    return {"mensagem": "Usuário registrado com sucesso!"} 

@router.post("/login")
def logar(usuario: UsuarioLogin):
    autenticado = autenticar_usuario(usuario.username, usuario.password)

    if not autenticado:
        raise HTTPException(status_code=400, detail='Usuário ou Senha Inválidos')

    access_token = criar_token(
        data={"sub":autenticado["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"token": access_token} 