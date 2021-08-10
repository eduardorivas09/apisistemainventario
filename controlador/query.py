from graphene import ObjectType, relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from schemas.producto import producObjeto
from schemas.cliente import clienteObjeto
from schemas.venta import ventaObjeto
from schemas.detalleventa import ventaDetalleObjeto

class Query(ObjectType):
    node = relay.Node.Field()
    allproducto = SQLAlchemyConnectionField(producObjeto.connection)
    allcliente = SQLAlchemyConnectionField(clienteObjeto.connection)
    allventa = SQLAlchemyConnectionField(ventaObjeto.connection)
    allventa_detalle = SQLAlchemyConnectionField(ventaDetalleObjeto.connection)  