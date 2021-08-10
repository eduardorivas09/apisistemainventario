from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.cliente import Cliente

class clienteObjeto(SQLAlchemyObjectType):
    class Meta:
        model = Cliente
        interfaces = (relay.Node,)
