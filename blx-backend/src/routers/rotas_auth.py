from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Usuario, UsuarioSimples, LoginData, LoginSucesso
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples) 
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    #verificar se já existe um usuario para o telefone
    usuario_localizado = RepositorioUsuario(session).obter_por_telefone(usuario.telefone)

    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Telefone já cadastrado")
    

    # Cria novo usuario
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get("/usuarios", status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios

@router.post("/token", status_code=status.HTTP_200_OK, response_model=LoginSucesso)
def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    # if not hash_provider.verificar_hash(login_data.senha, usuario.senha):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Senha incorreta")
    # return usuario
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Senha incorreta ou nao encontrada")

    # Gerar Token JWT
    token = token_provider.criar_access_token({"sub": usuario.telefone})
    return {"usuario": usuario, "access_token": token}
    # return LoginSucesso(usuario=usuario, access_token=token)

@router.get("/me", status_code=status.HTTP_200_OK, response_model=UsuarioSimples)
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario
    # return {"token": token}