from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.producto import Producto

class producObjeto(SQLAlchemyObjectType):
    class Meta:
        model = Producto
        interfaces = (relay.Node,)