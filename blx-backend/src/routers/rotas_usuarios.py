from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post("/usuarios", status_code=status.HTTP_201_CREATED) 
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get("/usuarios", status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
