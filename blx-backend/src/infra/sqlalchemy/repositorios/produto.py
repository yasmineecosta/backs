from sqlalchemy.orm import Session # orm = Object Relational Mapping
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

# Repositório de Produto
class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        # Instanciando um objeto do tipo Produto - models.Produto
        db_produto = models.Produto(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel) 
        self.db.add(db_produto) # Adicionando o objeto ao banco de dados
        self.db.commit() # Commitando a transação
        self.db.refresh(db_produto) # Atualizando o objeto
        return db_produto # Retornando o objeto

    def listar(self):
        produtos = self.db.query(models.Produto).all() # Listando todos os produtos
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass