from Conexion.base import Base
from models.detalleventa import VentaDetalle
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship, backref

class Producto(Base):

    __tablename__ = 'producto'
    idProducto = Column(Integer, primary_key = True)
    nombreProducto = Column(String(), nullable=False)
    stock = Column(Integer(), default=0)
    precio = Column(Float(), nullable=False)
    fechaCreacion = Column(Date())
    fechaVencimiento = Column(Date())
    Venta_detalle = relationship(VentaDetalle, backref= 'producto')

    def __init__(self, nombreProducto, stock, precio, fechaCreacion, fechaVencimiento):
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.stock = stock
        self.fechaCreacion = fechaCreacion
        self.fechaVencimiento = fechaVencimiento