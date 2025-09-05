# main.py
#python -m uvicorn app.main:app --port 8001 --reload
# GET http://localhost:8000

from fastapi import FastAPI
from .routers import calculadora, usuarios, viacep

app = FastAPI(title="Calculadora Modularizada", 
              description="Minha Calculadora", 
              version="6.0.0")

app.include_router(calculadora.router)
app.include_router(usuarios.router)
app.include_router(viacep.router)