from Conexion.base import Base
from models.venta import Venta
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref ,relationship

class Cliente(Base):

    __tablename__ = 'cliente'
    idCliente = Column(Integer, primary_key=True)
    nombre = Column(String(), nullable = False)
    apellido = Column(String(), nullable = False)
    correo = Column(String())
    venta = relationship(Venta, backref= 'cliente')

    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo