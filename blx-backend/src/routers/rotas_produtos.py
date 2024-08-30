from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Produto, ProdutoPutList
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()


# ROTAS DE PRODUTOS
# @app.post("/produtos", status_code=201) @app.post("/produtos", status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
@router.post("/produtos", status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

# @app.get("/produtos", status_code=status.HTTP_200_OK, response_model=List[Produto])
@router.get("/produtos", status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.put("/produtos/{id}", response_model=ProdutoPutList) 
def atualizar_produto(id: int, produto: ProdutoPutList, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    # return produto_atualizado
    return {"message": "Produto atualizado com sucesso!"}

@router.delete("/produtos/{id}")
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {"message": "Produto removido com sucesso!"}
