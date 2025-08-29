# app/auth.py
from .database import usuarios
from passlib.context import CryptContext
from datetime import datetime, timedelta
from .config import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_usuario(username: str):
    return usuarios.find_one({"username":username})

def gerar_hash(password: str):
    return pwd_context.hash(password)

def verificar_senha(password: str, hash: str):
    return pwd_context.verify(password, hash)

def autenticar_usuario(username: str, password: str):
    usuario = get_usuario(username)
    if not usuario:
        return False

    if not verificar_senha(password, usuario["password"]):
        return False
    
    return usuario


def criar_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)