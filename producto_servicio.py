#aplicar las reglas del negocio
from modelo import Producto


class ProductoServicio:

    def __init__(self, dao):
        self.dao = dao

# 1. Registrar
    def registrar(self, nombre, precio, stock):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        producto = Producto(None, nombre.strip(), precio, stock)

        return self.dao.crear(producto)

#2 Listar
    def listar(self):
        return self.dao.listar()

#3 Buscar por id
    def buscar_id(self, id):
        producto = self.dao.buscar_id(id)

        if producto is None:
            raise ValueError("El producto no existe")

        return producto

#4 Actualizar 
    def actualizar(self, id, nombre, precio, stock):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        producto = self.dao.buscar_id(id)
        if producto is None:
            raise ValueError("El producto no existe")
        
        producto.nombre = nombre.strip()
        producto.precio = precio
        producto.stock = stock
        self.dao.actualizar(producto)

#5 Eliminar
    def eliminar(self, id):
        eliminado = self.dao.eliminar(id)

        if not eliminado:
            raise ValueError("El ID no existe")

#6 Vender
    def vender(self, id, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        producto = self.dao.buscar_id(id)

        if producto is None:
            raise ValueError("El producto no existe")

        if cantidad > producto.stock:
            raise ValueError("No hay suficiente stock")

        producto.stock = producto.stock - cantidad
        self.dao.actualizar(producto)

        return producto
    
