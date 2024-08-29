from pydantic import BaseModel
from typing import Optional
from typing import List

class Usuario(BaseModel):
    id: str
    nome: str
    telefone: str
    # meus_produtos: List[Produto]
    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]

class Produto(BaseModel):
    id: str
    # usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Confir:
        orm_mode = True

class Pedido(BaseModel):
    id: str
    usuario: Usuario
    # produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacao: str = 'Sem observações'


