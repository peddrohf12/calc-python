# app/auth.py
from .database import usuarios
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_usuario(username: str):
    return usuarios.find_one({"username":username})

def gerar_hash(password: str):
    return pwd_context.hash(password)