import graphene
from models.producto import Producto
from models.cliente import Cliente
from models.venta import Venta
from models.detalleventa import VentaDetalle
from schemas.producto import producObjeto
from schemas.cliente import clienteObjeto
from schemas.venta import ventaObjeto
from schemas.detalleventa import ventaDetalleObjeto
from Conexion.db_session import db_session

#Mutation de agregrar

class agregarProducto(graphene.Mutation):
    class Arguments:
        nombreProducto = graphene.String()
        stock = graphene.Int()
        precio = graphene.Float()
        fechaCreacion = graphene.Date()
        fechaVencimiento = graphene.Date()
    
    nuevoProducto = graphene.Field(lambda: producObjeto)

    def mutate(self, info, nombreProducto, stock, precio, fechaCreacion, fechaVencimiento):
        nuevoProducto = Producto(nombreProducto= nombreProducto, stock= stock, precio= precio, fechaCreacion = fechaCreacion, fechaVencimiento = fechaVencimiento)
        db_session.session.add(nuevoProducto)
        db_session.session.commit()
        return agregarProducto(nuevoProducto = nuevoProducto)

class agregarCliente(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        email = graphene.String()
    
    nuevoCliente = graphene.Field(lambda: clienteObjeto)
    
    def mutate(self,info, nombre, apellido, email):
        nuevoCliente = Cliente(nombre= nombre, apellido= apellido, correo= email)
        db_session.session.add(nuevoCliente)
        db_session.session.commit()
        return agregarCliente(nuevoCliente = nuevoCliente)

class agregarVenta(graphene.Mutation):
    class Arguments:
        clienteId = graphene.Int()
        fechaVenta = graphene.Date()

    nuevaVenta = graphene.Field(lambda: ventaObjeto)

    def mutate(self, info, clienteId, fechaVenta):
        nuevaVenta = Venta(clienteId, fechaVenta)
        db_session.session.add(nuevaVenta)
        db_session.session.commit()
        return agregarVenta(nuevaVenta = nuevaVenta)

class agregarDetalleVenta(graphene.Mutation):
    class Arguments:
        idVenta = graphene.Int()
        idProducto = graphene.Int()
        cantidad = graphene.Int()

    nuevaDetalleVenta = graphene.Field(lambda: ventaDetalleObjeto)

    def mutate(self, info, idVenta, idProducto, cantidad):
        nuevaDetalleVenta  = VentaDetalle(idVenta, idProducto, cantidad)
        db_session.session.add(nuevaDetalleVenta)
        db_session.session.commit()
        return agregarDetalleVenta(nuevaDetalleVenta = nuevaDetalleVenta)

#Mutation Update

class actualizarProducto(graphene.Mutation):
    class Arguments:
        idProducto = graphene.Int()
        nombreProducto = graphene.String()
        stock = graphene.Int()
        precio = graphene.Float()
        fechaCreacion = graphene.Date()
        fechaVencimiento = graphene.Date()
    
    updateProducto = graphene.Field(lambda: producObjeto)

    def mutate(self, info,idProducto, nombreProducto, stock, precio, fechaCreacion, fechaVencimiento):

        updateProducto = Producto.query.get(idProducto)
        updateProducto.nombreProducto = nombreProducto
        updateProducto.stock = stock
        updateProducto.precio = precio
        updateProducto.fechaCreacion = fechaCreacion
        updateProducto.fechaVencimiento = fechaVencimiento

        db_session.session.add(updateProducto)
        db_session.session.commit()
        return actualizarProducto(updateProducto = updateProducto)

class actualizarCliente(graphene.Mutation):
    class Arguments:
        idCliente = graphene.Int()
        nombre = graphene.String()
        apellido = graphene.String()
        email = graphene.String()
    
    updateCliente = graphene.Field(lambda: clienteObjeto)
    
    def mutate(self,info,idCliente, nombre, apellido, email):
        updateCliente = Cliente.query.get(idCliente)
        
        updateCliente.nombre = nombre
        updateCliente.apellido = apellido
        updateCliente.email = email
        db_session.session.add(updateCliente)
        db_session.session.commit()
        return actualizarCliente(updateCliente = updateCliente)

class actualizarVenta(graphene.Mutation):
    class Arguments:
        ventaId = graphene.Int()
        clienteId = graphene.Int()
        fechaVenta = graphene.Date()

    updateVenta = graphene.Field(lambda: ventaObjeto)

    def mutate(self, info, ventaId, clienteId, fechaVenta):
        updateVenta = Venta.query.get(ventaId)

        updateVenta.clienteId = clienteId
        updateVenta.fechaVenta = fechaVenta
        
        db_session.session.add(updateVenta)
        db_session.session.commit()
        return actualizarVenta(updateVenta = updateVenta)

class actualizarDetalleVenta(graphene.Mutation):
    class Arguments:
        idVentaDetalle = graphene.Int()
        idVenta = graphene.Int()
        idProducto = graphene.Int()
        cantidad = graphene.Int()
        
    updateDetalleVenta = graphene.Field(lambda: ventaDetalleObjeto)

    def mutate(self, info, idVentaDetalle, idVenta, idProducto, cantidad):
        updateDetalleVenta = VentaDetalle.query.get(idVentaDetalle)

        updateDetalleVenta.idVenta = idVenta
        updateDetalleVenta.productoId = idProducto
        updateDetalleVenta.cantidad = cantidad

        db_session.session.add(updateDetalleVenta)
        db_session.session.commit()
        return actualizarDetalleVenta(updateDetalleVenta = updateDetalleVenta)

# Eliminar

class eliminarProducto(graphene.Mutation):
    class Arguments:
        idProducto = graphene.Int()
    
    deleteProducto = graphene.Field(lambda: producObjeto)

    def mutate(self, info, idProducto):

        deleteProducto = Producto.query.get(idProducto)

        db_session.session.delete(deleteProducto)
        db_session.session.commit()
        return eliminarProducto(deleteProducto = deleteProducto)

class eliminarCliente(graphene.Mutation):
    class Arguments:
        idCliente = graphene.Int()
    
    deleteCliente = graphene.Field(lambda: clienteObjeto)
    
    def mutate(self,info, idCliente):
        deleteCliente = Cliente.query.get(idCliente)

        db_session.session.delete(deleteCliente)
        db_session.session.commit()
        return eliminarCliente(deleteCliente = deleteCliente)

class eliminarVenta(graphene.Mutation):
    class Arguments:
        ventaId = graphene.Int()

    deleteVenta = graphene.Field(lambda: ventaObjeto)

    def mutate(self, info, ventaId):
        deleteVenta = Venta.query.get(ventaId)
        
        db_session.session.delete(deleteVenta)
        db_session.session.commit()
        return eliminarVenta(deleteVenta = deleteVenta)

class eliminarDetalleVenta(graphene.Mutation):
    class Arguments:
        idVentaDetalle = graphene.Int()
        
    deleteDetalleVenta = graphene.Field(lambda: ventaDetalleObjeto)

    def mutate(self, info, idVentaDetalle):
        deleteDetalleVenta = VentaDetalle.query.get(idVentaDetalle)

        db_session.session.delete(deleteDetalleVenta)
        db_session.session.commit()
        return eliminarDetalleVenta(deleteDetalleVenta = deleteDetalleVenta)

class Mutation(graphene.ObjectType):
    addCliente = agregarCliente.Field()
    addProducto = agregarProducto.Field()
    addVenta = agregarVenta.Field()
    addVentaDetalle = agregarDetalleVenta.Field()
    updateProducto = actualizarProducto.Field()
    updateCliente = actualizarCliente.Field()
    updateVenta = actualizarVenta.Field()
    updateVentaDetalle = actualizarDetalleVenta.Field()
    deleteProducto = eliminarProducto.Field()
    deleteCliente = eliminarCliente.Field()
    deleteVenta = eliminarVenta.Field()
    deleteVentaDetalle = eliminarDetalleVenta.Field()