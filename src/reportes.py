from datetime import datetime
from math import isfinite

from inventario import consultar_stock_minimo
from productos import listar_productos
from ventas import mostrar_venta


def historial_ventas(ventas):
    if not ventas:
        print("No hay ventas registradas.")
        return
    for venta in ventas:
        mostrar_venta(venta)


def total_ingresos(ventas):
    total = 0.0
    for venta in ventas:
        total += venta["total"]
    if not isfinite(total):
        return None
    return round(total, 2)


def reporte_ingresos(ventas):
    total = total_ingresos(ventas)
    if total is None:
        print("El importe excede el rango numérico.")
    else:
        print(f"Total de ingresos por ventas (incluye IVA): {total:.2f}")


def productos_mas_vendidos(ventas):
    # Sumar las unidades vendidas de cada producto.
    acumulados = {}
    for venta in ventas:
        for linea in venta["detalle"]:
            codigo = linea["codigo"]
            if codigo not in acumulados:
                acumulados[codigo] = {"codigo": codigo,
                                      "nombre": linea["nombre"],
                                      "cantidad": 0}
            acumulados[codigo]["cantidad"] += linea["cantidad"]

    mayor = 0
    for producto in acumulados.values():
        if producto["cantidad"] > mayor:
            mayor = producto["cantidad"]

    ganadores = []
    for producto in acumulados.values():
        if producto["cantidad"] == mayor:
            ganadores.append(producto)
    return ganadores


def reporte_mas_vendido(ventas):
    ganadores = productos_mas_vendidos(ventas)
    if not ganadores:
        print("No hay ventas registradas.")
        return
    print("Productos con mayor cantidad de unidades vendidas:")
    for producto in ganadores:
        print(f"{producto['codigo']} - {producto['nombre']} | Unidades: {producto['cantidad']}")


def valor_inventario(productos):
    total = 0.0
    try:
        for producto in productos:
            precio = round(producto["precio"], 2)
            valor = round(precio * producto["existencia"], 2)
            total += valor
    except OverflowError:
        return None
    if not isfinite(total):
        return None
    return round(total, 2)


def reporte_valor_inventario(productos):
    total = valor_inventario(productos)
    if total is None:
        print("El importe excede el rango numérico.")
    else:
        print(f"Valor del inventario a precio de venta (incluye inactivos): {total:.2f}")


def leer_fecha(campo):
    while True:
        texto = input(campo + " (YYYY-MM-DD, Enter para cancelar): ").strip()
        if texto == "":
            return None
        try:
            fecha = datetime.strptime(texto, "%Y-%m-%d").date()
            if fecha.isoformat() == texto:
                return fecha
        except ValueError:
            pass
        print("Fecha inválida. Usá YYYY-MM-DD con una fecha real.")


def resumen_periodo(ventas, inicio, fin):
    seleccionadas = []
    for venta in ventas:
        fecha = datetime.strptime(venta["fecha"][:10], "%Y-%m-%d").date()
        if inicio <= fecha <= fin:
            seleccionadas.append(venta)
    ingresos = total_ingresos(seleccionadas)
    if ingresos is None:
        return None
    dias = (fin - inicio).days + 1
    return {"ventas": len(seleccionadas), "dias": dias, "ingresos": ingresos,
            "promedio_ventas": len(seleccionadas) / dias,
            "promedio_ingresos": round(ingresos / dias, 2)}


def reporte_promedio(ventas):
    inicio = leer_fecha("Fecha inicial")
    if inicio is None:
        print("Reporte cancelado.")
        return
    while True:
        fin = leer_fecha("Fecha final")
        if fin is None:
            print("Reporte cancelado.")
            return
        if fin >= inicio:
            break
        print("La fecha final no puede ser anterior a la inicial.")
    resumen = resumen_periodo(ventas, inicio, fin)
    if resumen is None:
        print("El importe excede el rango numérico.")
        return
    print("Ventas del período:", resumen["ventas"])
    print("Días del período (incluye días sin ventas):", resumen["dias"])
    print(f"Ingresos del período (incluye IVA): {resumen['ingresos']:.2f}")
    print(f"Promedio de ventas por día: {resumen['promedio_ventas']:.2f}")
    print(f"Promedio de ingresos por día: {resumen['promedio_ingresos']:.2f}")


def menu_reportes(productos, ventas):
    while True:
        print("\nReportes y estadísticas")
        print("1. Listado general de productos.")
        print("2. Productos en stock mínimo o por debajo.")
        print("3. Historial de ventas.")
        print("4. Total de ingresos por ventas.")
        print("5. Producto con más unidades vendidas.")
        print("6. Valor total del inventario.")
        print("7. Promedio de ventas por período.")
        print("8. Volver al menú principal.")
        opcion = input("Seleccioná una opción: ").strip()
        if opcion == "1":
            listar_productos(productos)
        elif opcion == "2":
            consultar_stock_minimo(productos)
        elif opcion == "3":
            historial_ventas(ventas)
        elif opcion == "4":
            reporte_ingresos(ventas)
        elif opcion == "5":
            reporte_mas_vendido(ventas)
        elif opcion == "6":
            reporte_valor_inventario(productos)
        elif opcion == "7":
            reporte_promedio(ventas)
        elif opcion == "8":
            break
        else:
            print("Opción incorrecta. Ingresá un número del 1 al 8.")

