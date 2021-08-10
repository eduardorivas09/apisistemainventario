from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.detalleventa import VentaDetalle

class ventaDetalleObjeto(SQLAlchemyObjectType):
    class Meta:
        model = VentaDetalle
        interfaces = (relay.Node,)