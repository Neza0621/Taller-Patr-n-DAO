#ejecutar las operaciones sql
from base_datos import obtener_conexion
from modelo import Producto

class ProductoDAO:
    
#1. crear un producto
    def crear(self, producto):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            
            sql = """ 
                INSERT INTO productos (nombre, precio, stock)
                VALUES (?, ?, ?)
            """
            
            cursor.execute(sql,(producto.nombre, producto.precio, producto.stock))
            producto.id = cursor.lastrowid
            conexion.commit()
            return producto
        finally:
            conexion.close()
            
#2. Listar productos
    def listar(self):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()

            cursor.execute("SELECT id, nombre, precio, stock FROM productos")
            filas = cursor.fetchall()
        finally:
            conexion.close()

        productos = []
        for fila in filas:
            productos.append(self._convertir(fila))
        return productos

#3. Buscar por id
    def buscar_id(self, id):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
                (id,)
                )
            fila = cursor.fetchone()
        finally:
            conexion.close()

        if fila is None:
            return None
        return self._convertir(fila)

#4. Actualizar
    def actualizar(self, producto):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            sql = """
                UPDATE productos 
                SET nombre = ?, precio = ?, stock = ?
                WHERE id = ?
            """
            cursor.execute(
                sql, 
                (producto.nombre, producto.precio, producto.stock, producto.id)
            )
            conexion.commit()
            return cursor.rowcount > 0
        finally:
            conexion.close()

#5. Eliminar
    def eliminar(self, id):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()

            cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            conexion.commit()
            return cursor.rowcount > 0
        finally:
            conexion.close()

#5. Auxiliar: Convierte una tupla en un objeto "Producto"
    def _convertir(self, fila):
        return Producto(fila[0], fila[1], fila[2], fila[3])