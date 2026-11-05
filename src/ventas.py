from math import isfinite

from estructuras import crear_movimiento, fecha_actual
from productos import buscar_producto, leer_entero


def mostrar_venta(venta):
    if "numero" in venta:
        print("\nVenta número:", venta["numero"])
        print("Fecha:", venta["fecha"])
    for linea in venta["detalle"]:
        print(f"{linea['codigo']} - {linea['nombre']} | Cantidad: {linea['cantidad']} | "
              f"Precio: {linea['precio_unitario']:.2f} | Subtotal: {linea['subtotal']:.2f}")
    print(f"Subtotal: {venta['subtotal']:.2f}")
    print(f"IVA (12 %): {venta['iva']:.2f}")
    print(f"Total: {venta['total']:.2f}")


def registrar_venta(productos, ventas, movimientos=None):
    disponible = False
    for producto in productos:
        if producto["activo"] and producto["existencia"] > 0:
            disponible = True
    if not disponible:
        print("No hay productos activos con existencias para vender.")
        return

    detalle = []
    while True:
        codigo = input("Código del producto (Enter para finalizar): ").strip().upper()
        if codigo == "":
            break
        producto = buscar_producto(productos, codigo)
        if producto is None:
            print("No existe un producto con ese código.")
            continue
        if not producto["activo"]:
            print("El producto está inactivo.")
            continue

        linea_anterior = None
        reservada = 0
        for linea in detalle:
            if linea["codigo"] == codigo:
                linea_anterior = linea
                reservada = linea["cantidad"]
        restante = producto["existencia"] - reservada
        if restante == 0:
            print("No hay más existencias disponibles de ese producto.")
            continue
        print("Producto:", producto["nombre"])
        print(f"Precio unitario: {producto['precio']:.2f}")
        print("Disponible para agregar:", restante)
        while True:
            cantidad = leer_entero("Cantidad a vender")
            if cantidad == 0:
                print("La cantidad debe ser mayor que cero.")
            elif cantidad > restante:
                print("Inventario insuficiente para esa cantidad.")
            else:
                break

        precio = round(producto["precio"], 2)
        try:
            subtotal_producto = round(precio * (reservada + cantidad), 2)
            nuevo_subtotal = subtotal_producto
            for linea in detalle:
                if linea["codigo"] != codigo:
                    nuevo_subtotal += linea["subtotal"]
            nuevo_subtotal = round(nuevo_subtotal, 2)
            nuevo_iva = round(nuevo_subtotal * 0.12, 2)
            nuevo_total = round(nuevo_subtotal + nuevo_iva, 2)
        except OverflowError:
            print("El importe excede el rango numérico. No se agregó el producto.")
            continue
        if not isfinite(nuevo_subtotal) or not isfinite(nuevo_iva) or not isfinite(nuevo_total):
            print("El importe excede el rango numérico. No se agregó el producto.")
            continue

        # Usar los nuevos totales solo si el cálculo es válido.
        subtotal = nuevo_subtotal
        iva = nuevo_iva
        total = nuevo_total

        if linea_anterior is None:
            detalle.append({
                "codigo": codigo, "nombre": producto["nombre"],
                "precio_unitario": precio, "cantidad": cantidad,
                "subtotal": subtotal_producto,
            })
        else:
            linea_anterior["cantidad"] += cantidad
            linea_anterior["subtotal"] = subtotal_producto

    if not detalle:
        print("Venta cancelada. No se agregaron productos.")
        return
    venta = {"detalle": detalle, "subtotal": subtotal, "iva": iva, "total": total}
    mostrar_venta(venta)
    while True:
        respuesta = input("¿Confirmar venta? (S/N): ").strip().upper()
        if respuesta == "N":
            print("Venta cancelada.")
            return
        if respuesta == "S":
            break
        print("Respuesta inválida. Ingresá S o N.")

    venta["numero"] = len(ventas) + 1
    venta["fecha"] = fecha_actual()
    nuevos_movimientos = []
    if movimientos is not None:
        for linea in detalle:
            nuevos_movimientos.append(crear_movimiento(
                linea["codigo"], "Salida por venta", linea["cantidad"],
                "Venta número " + str(venta["numero"]), venta["fecha"]))
    for linea in detalle:
        producto = buscar_producto(productos, linea["codigo"])
        producto["existencia"] -= linea["cantidad"]
    ventas.append(venta)
    if movimientos is not None:
        for movimiento in nuevos_movimientos:
            movimientos.append(movimiento)
    print("Venta registrada correctamente. Número:", venta["numero"])

