import sqlalchemy
from Conexion.base import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, backref

class VentaDetalle(Base):

    __tablename__ = 'ventaDetalle'
    idVentaDetalle = Column(Integer, primary_key=True)
    idVenta = Column(Integer(),ForeignKey('venta.idVenta'))
    productoId = Column(Integer(), ForeignKey('producto.idProducto')) 
    Cantidad = Column(Integer())

    def __init__(self, idventa, productoId, cantidad):
        self.idVenta = idventa
        self.productoId = productoId
        self.Cantidad = cantidad