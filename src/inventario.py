from estructuras import crear_movimiento
from productos import buscar_producto, leer_entero, leer_texto, pedir_codigo


def mostrar_existencia(producto):
    if producto["activo"]:
        estado = "Activo"
    else:
        estado = "Inactivo"
    print(f"{producto['codigo']} - {producto['nombre']} | Cantidad: {producto['existencia']} | "
          f"Mínimo: {producto['stock_minimo']} | Estado: {estado}")


def consultar_existencias(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        mostrar_existencia(producto)


def productos_con_stock_minimo(productos):
    bajos = []
    for producto in productos:
        if producto["existencia"] <= producto["stock_minimo"]:
            bajos.append(producto)
    return bajos


def consultar_stock_minimo(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    bajos = productos_con_stock_minimo(productos)
    if not bajos:
        print("No hay productos en el stock mínimo o por debajo.")
        return
    for producto in bajos:
        mostrar_existencia(producto)


def registrar_entrada(productos, movimientos):
    if not productos:
        print("No hay productos registrados.")
        return
    producto = buscar_producto(productos, pedir_codigo())
    if producto is None:
        print("No existe un producto con ese código.")
        return
    mostrar_existencia(producto)
    while True:
        cantidad = leer_entero("Cantidad de entrada")
        if cantidad > 0:
            break
        print("La cantidad debe ser mayor que cero.")
    descripcion = leer_texto("Descripción", "La descripción es obligatoria.")
    print("Cantidad resultante:", producto["existencia"] + cantidad)
    while True:
        respuesta = input("¿Confirmar entrada? (S/N): ").strip().upper()
        if respuesta == "N":
            print("Entrada cancelada.")
            return
        if respuesta == "S":
            break
        print("Respuesta inválida. Ingresá S o N.")
    movimiento = crear_movimiento(producto["codigo"], "Entrada", cantidad, descripcion)
    producto["existencia"] += cantidad
    movimientos.append(movimiento)
    print("Entrada registrada correctamente. Cantidad disponible:", producto["existencia"])


def consultar_movimientos(movimientos):
    if not movimientos:
        print("No hay movimientos registrados.")
        return
    for movimiento in movimientos:
        print(f"{movimiento['fecha']} | {movimiento['codigo']} | {movimiento['tipo']} | "
              f"Cantidad: {movimiento['cantidad']} | {movimiento['descripcion']}")


def menu_inventario(productos, movimientos):
    while True:
        print("\nControl de inventario")
        print("1. Consultar existencias.")
        print("2. Registrar entrada.")
        print("3. Productos en stock mínimo o por debajo.")
        print("4. Historial de movimientos.")
        print("5. Volver al menú principal.")
        opcion = input("Seleccioná una opción: ").strip()
        if opcion == "1":
            consultar_existencias(productos)
        elif opcion == "2":
            registrar_entrada(productos, movimientos)
        elif opcion == "3":
            consultar_stock_minimo(productos)
        elif opcion == "4":
            consultar_movimientos(movimientos)
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta. Ingresá un número del 1 al 5.")

