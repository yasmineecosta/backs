from sqlalchemy.orm import Session # orm = Object Relational Mapping
from src.schemas import schemas
from typing import List
from src.infra.sqlalchemy.models import models
from sqlalchemy import update, delete, select
from sqlalchemy.sql.functions import mode
import random

class RepositorioPedido():
    
    def __init__(self, session: Session) -> None:
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido) -> models.Pedido:
        # usuario = await self.session.execute(select(models.Usuario).where(models.Usuario.id == pedido.usuario_id))
        # produto = await self.session.execute(select(models.Produto).where(models.Produto.id == pedido.produto_id))
        pedido_bd = models.Pedido(id=random.randint(1, 100) ,quantidade=pedido.quantidade, local_entrega=pedido.local_entrega, tipo_entrega=pedido.tipo_entrega, observacao=pedido.observacao, usuario_id=pedido.usuario_id, produto_id=pedido.produto_id)
        self.session.add(pedido_bd)
        self.session.commit()
        self.session.refresh(pedido_bd)
        return pedido_bd
    
    def buscar_por_id(self, id: int) -> models.Pedido:
        query = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(query).scalars().one()
        return pedido
    
    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        query = select(models.Pedido).where(models.Pedido.usuario_id == usuario_id)
        pedidos = self.session.execute(query).scalars().all()
        return pedidos
    
    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        query = select(models.Pedido).join_from(models.Pedido, models.Produto).where(models.Produto.usuario_id == usuario_id)
        pedidos = self.session.execute(query).scalars().all()
        # pedidos = self.session.execute(query).all()
        return pedidos
    
