from inventario import menu_inventario
from productos import menu_productos
from reportes import menu_reportes
from ventas import registrar_venta


def mostrar_menu():
    print("\nSistema de gestión comercial")
    print("1. Gestión de productos.")
    print("2. Registro de ventas.")
    print("3. Control de inventario.")
    print("4. Reportes y estadísticas.")
    print("5. Salir.")


def main():
    # Los módulos usan estas mismas listas mientras el programa está abierto.
    productos = []
    ventas = []
    movimientos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "1":
            menu_productos(productos, movimientos)
        elif opcion == "2":
            registrar_venta(productos, ventas, movimientos)
        elif opcion == "3":
            menu_inventario(productos, movimientos)
        elif opcion == "4":
            menu_reportes(productos, ventas)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción incorrecta. Ingresá un número del 1 al 5.")


if __name__ == "__main__":
    main()

