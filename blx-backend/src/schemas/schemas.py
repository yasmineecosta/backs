from pydantic import BaseModel
from typing import Optional
from typing import List
# modelos de dados que vao chegar e sair da api
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


class LoginData(BaseModel):
    senha: str
    telefone: str

class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str
    
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
    # usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[int]
    quantidade: int
    local_entrega: str
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'
    
    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoPutList]
    class Config:
        orm_mode = True

class PedidoPost(BaseModel):
    id: Optional[int]
    quantidade: int
    local_entrega: str
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'
    
    usuario_id: Optional[int]
    produto_id: Optional[int]

    class Config:
        orm_mode = True


