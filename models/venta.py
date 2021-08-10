from Conexion.base import Base
from models.detalleventa import VentaDetalle
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, backref

class Venta(Base):

    __tablename__ = 'venta'
    idVenta = Column(Integer, primary_key =True)
    clienteId = Column(Integer, ForeignKey('cliente.idCliente'))
    fechaVenta = Column(Date)
    ventaDetalle = relationship(VentaDetalle, backref= 'venta')
    
    def __init__(self, clienteId, fechaVenta):
       self.clienteId = clienteId
       self.fechaVenta = fechaVenta