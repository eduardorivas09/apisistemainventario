from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.venta import Venta

class ventaObjeto(SQLAlchemyObjectType):
    class Meta:
        model = Venta
        interfaces = (relay.Node,)