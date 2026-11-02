# mostrar el menu y recibir datos
import os
from base_datos import inicializar_bd
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio

dao = ProductoDAO()
servicio = ProductoServicio(dao)

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona Enter para continuar...")

def pedir_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número entero")

def registrar():
    nombre = input("Nombre: ")
    precio = pedir_entero("Precio: ")
    stock = pedir_entero("Stock: ")
    producto = servicio.registrar(nombre, precio, stock)
    print(f"Registrado con exito...\n ID: {producto.id}")

def mostrar():
    productos = servicio.listar()
    if not productos:
        print("¡El inventario esta vacío!")
    for p in productos:
        print(f"ID: {p.id} | {p.nombre} | ${p.precio} | Stock: {p.stock}")

def buscar():
    id = pedir_entero("Ingrese el ID del producto que desea buscar: ")
    p = servicio.buscar_id(id)
    print(f"ID: {p.id} | {p.nombre} | ${p.precio} | Stock: {p.stock}")

def actualizar():
    id = pedir_entero("Ingrese ID del producto que desea actualizar: ")
    nombre = input("Nuevo nombre: ")
    precio = pedir_entero("Nuevo precio: ")
    stock = pedir_entero("Nuevo stock: ")
    servicio.actualizar(id, nombre, precio, stock)
    print("¡Actualizado con exito!")

def eliminar():
    id = pedir_entero("Ingrese el ID del producto que desea eliminar: ")
    servicio.eliminar(id)
    print("¡Eliminado con exito!")
    
def vender():
    id = pedir_entero("Ingrese el ID del producto que desea vender: ")
    cantidad = pedir_entero("Cantidad a vender: ")
    p = servicio.vender(id, cantidad)
    print(f"¡Vendido con exito!\nStock restante: {p.stock}")

def menu():
    while True:
        print("\n====== MENÚ ======")
        print("1. Registrar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar videojuego")
        print("5. Eliminar videojuego")
        print("6. Vender unidades")
        print("7. Salir")

        opcion = input("Elige una opción: ")
        try:
            match opcion:
                case "1":
                    registrar()
                case "2":
                    mostrar()
                case "3":
                    buscar()
                case "4":
                    actualizar()
                case "5":
                    eliminar()
                case "6":
                    vender()
                case "7":
                    limpiar()
                    print("Hasta Luego...")
                    break
                case _:
                    print("Opción inválida")

        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

        pausar()

if __name__ == "__main__":
    # Preparar la base de datos
    inicializar_bd()
    limpiar()
    menu()
