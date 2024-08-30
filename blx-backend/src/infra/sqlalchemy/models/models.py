from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    produtos = relationship('Produto', back_populates='usuario') # Relacionamento com a tabela Produto
    
# tabela no banco de dados
class Produto(Base):

    __tablename__ = 'produto' # Nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario')) # Chave estrangeira
    
    usuario = relationship('Usuario', back_populates='produtos') # Relacionamento com a tabela Usuario
