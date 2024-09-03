from sqlalchemy.orm import Session # orm = Object Relational Mapping
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import update, delete, select
import uuid
import random

# Repositório de Produto
class RepositorioProduto():

    def __init__(self, db: Session):
        self.session = db

    def criar(self, produto: schemas.ProdutoSimplesAtt):
        # Instanciando um objeto do tipo Produto - models.Produto
        # usuario = await self.session.execute(select(models.Usuario).where(models.Usuario.id == produto.usuario_id))
        db_produto = models.Produto(id=random.randint(1, 100), nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel, usuario_id=produto.usuario_id) # , usuario=usuario
        self.session.add(db_produto) # Adicionando o objeto ao banco de dados
        self.session.commit() # Commitando a transação
        self.session.refresh(db_produto) # Atualizando o objeto
        return db_produto # Retornando o objeto

    def listar(self):
        produtos = self.session.query(models.Produto).all() # Listando todos os produtos
        return produtos

    def editar(self, id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto).where(models.Produto.id == id).values(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel)
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, id: int):
        delete_stmt = delete(models.Produto).where(models.Produto.id == id)
        self.session.execute(delete_stmt)
        self.session.commit()

    def buscar_por_id(self, id: int):
        consulta = select(models.Produto).where(models.Produto.id == id)
        produto = self.session.execute(consulta).first()
        return produto

    def obter(self):
        pass