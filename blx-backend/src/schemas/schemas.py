from pydantic import BaseModel
from typing import Optional
from typing import List

class ProdutoPutList(BaseModel):
    id: Optional[int]
    nome: str
    preco: float
    disponivel: bool
    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoPutList] = []
    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    # id: str
    usuario: Usuario
    nome: str
    preco: float
    # disponivel: bool
    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    # usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    usuario: Optional[UsuarioSimples]
    # usuario: Usuario
    class Config:
        orm_mode = True

class ProdutoSimplesAtt(BaseModel):
    nome: str
    preco: float

    class Config:
        orm_mode = True
class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacao: Optional[str] = 'Sem observações'


