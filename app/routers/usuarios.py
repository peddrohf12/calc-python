# app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException, Body
from ..models import UsuarioLogin, UsuarioCadastro
from ..auth import get_usuario, gerar_hash, autenticar_usuario, criar_token, get_usuario_atual
from ..database import usuarios
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from ..viacep import buscar_cep
from bson import ObjectId


router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/test")
def test():
    return {"mensagem": "OK, tudo certo!"}


@router.post("/registro")
def registrar(usuariox: UsuarioCadastro):
    if get_usuario(usuariox.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")

    dadosCep = buscar_cep(usuariox.cep)
    if not dadosCep or "erro" in dadosCep:
        raise HTTPException(status_code=400, detail="CEP inválido")

    hash_senha = gerar_hash(usuariox.password)

    usuarios.insert_one({
        "username": usuariox.username,
        "password": hash_senha,
        "cep": usuariox.cep,
        "numero": usuariox.numero,
        "complemento": usuariox.complemento,
        "logradouro": dadosCep.get("logradouro", ""),
        "bairro": dadosCep.get("bairro", ""),
        "localidade": dadosCep.get("localidade", ""),
        "uf": dadosCep.get("uf", "")
    })

    return {"mensagem": "Usuário registrado com sucesso!"}


@router.post("/login")
def logar(usuario: UsuarioLogin):
    autenticado = autenticar_usuario(usuario.username, usuario.password)

    if not autenticado:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")

    access_token = criar_token(
        data={"sub": autenticado["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"token": access_token, "expires": timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)} 

@router.get("/")
def listar_usuarios():
    lista = []
    for usuario in usuarios.find({}, {"password":0}): 

        usuario["_id"] = str(usuario["_id"])

        lista.append(usuario)
    return lista
    