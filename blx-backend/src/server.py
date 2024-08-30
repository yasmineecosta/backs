# Rotas e controller
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
# from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.routers import rotas_produtos, rotas_usuarios

# criar_bd()

app = FastAPI()

origins = ["http://127.0.0.1:8000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, 
                   allow_methods=["*"], allow_headers=["*"])

# # ROTAS DE PRODUTOS
app.include_router(rotas_produtos.router)

# ROTAS DE USUARIOS
app.include_router(rotas_usuarios.router)