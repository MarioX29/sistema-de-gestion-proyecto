from math import isfinite

from estructuras import crear_movimiento


def es_numero(texto, permitir_punto):
    digitos = 0
    puntos = 0
    for caracter in texto:
        if caracter in "0123456789":
            digitos += 1
        elif caracter == "." and permitir_punto:
            puntos += 1
        else:
            return False
    return digitos > 0 and puntos <= 1


def leer_texto(campo, aviso, anterior=None):
    while True:
        indicacion = ""
        if anterior is not None:
            indicacion = " (Enter para conservar)"
        texto = input(campo + indicacion + ": ").strip()
        if texto == "" and anterior is not None:
            return anterior
        if texto != "":
            return texto
        print(aviso)


def leer_precio(anterior=None):
    while True:
        indicacion = ""
        if anterior is not None:
            indicacion = " (Enter para conservar)"
        texto = input("Precio" + indicacion + ": ").strip()
        if texto == "" and anterior is not None:
            return anterior
        if es_numero(texto, True):
            precio = float(texto)
            if isfinite(precio) and precio >= 0:
                return precio
        print("Precio inválido. Usá cero o un número positivo con punto decimal; no se acepta infinito.")


def leer_entero(campo, anterior=None):
    while True:
        indicacion = ""
        if anterior is not None:
            indicacion = " (Enter para conservar)"
        texto = input(campo + indicacion + ": ").strip()
        if texto == "" and anterior is not None:
            return anterior
        if len(texto) <= 4300 and es_numero(texto, False):
            try:
                return int(texto)
            except ValueError:
                pass
        print(campo + ": valor inválido. Usá un entero desde cero y dentro del rango permitido.")


def buscar_producto(productos, codigo):
    codigo = codigo.strip().upper()
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def pedir_codigo():
    return leer_texto("Código", "El código es obligatorio.").upper()


def registrar_producto(productos, movimientos=None):
    while True:
        codigo = pedir_codigo()
        if buscar_producto(productos, codigo) is None:
            break
        print("El código ya está registrado.")

    nombre = leer_texto("Nombre", "El nombre es obligatorio.")
    categoria = leer_texto("Categoría", "La categoría es obligatoria.")
    precio = leer_precio()
    existencia = leer_entero("Existencia inicial")
    stock_minimo = leer_entero("Stock mínimo")

    movimiento = None
    if movimientos is not None:
        movimiento = crear_movimiento(codigo, "Entrada inicial", existencia, "Registro del producto")

    productos.append({
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "existencia": existencia,
        "stock_minimo": stock_minimo,
        "activo": True,
    })
    if movimiento is not None:
        movimientos.append(movimiento)
    print("Producto registrado correctamente.")


def mostrar_producto(producto):
    print("\nCódigo:", producto["codigo"])
    print("Nombre:", producto["nombre"])
    print("Categoría:", producto["categoria"])
    print(f"Precio: {producto['precio']:.2f}")
    print("Cantidad disponible:", producto["existencia"])
    print("Stock mínimo:", producto["stock_minimo"])
    if producto["activo"]:
        print("Estado: Activo")
    else:
        print("Estado: Inactivo")


def consultar_producto(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    producto = buscar_producto(productos, pedir_codigo())
    if producto is None:
        print("No existe un producto con ese código.")
    else:
        mostrar_producto(producto)


def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        mostrar_producto(producto)


def modificar_producto(productos, movimientos=None):
    if not productos:
        print("No hay productos registrados.")
        return
    producto = buscar_producto(productos, pedir_codigo())
    if producto is None:
        print("No existe un producto con ese código.")
        return

    mostrar_producto(producto)
    nombre = leer_texto("Nombre", "El nombre es obligatorio.", producto["nombre"])
    categoria = leer_texto("Categoría", "La categoría es obligatoria.", producto["categoria"])
    precio = leer_precio(producto["precio"])
    existencia = leer_entero("Cantidad disponible", producto["existencia"])
    stock_minimo = leer_entero("Stock mínimo", producto["stock_minimo"])

    if (nombre == producto["nombre"] and categoria == producto["categoria"]
            and precio == producto["precio"] and existencia == producto["existencia"]
            and stock_minimo == producto["stock_minimo"]):
        print("No se realizaron cambios.")
        return

    movimiento = None
    diferencia = existencia - producto["existencia"]
    if movimientos is not None and diferencia != 0:
        if diferencia > 0:
            tipo = "Ajuste de entrada"
        else:
            tipo = "Ajuste de salida"
        movimiento = crear_movimiento(producto["codigo"], tipo, abs(diferencia),
                                      "Corrección de cantidad en gestión de productos")

    producto["nombre"] = nombre
    producto["categoria"] = categoria
    producto["precio"] = precio
    producto["existencia"] = existencia
    producto["stock_minimo"] = stock_minimo
    if movimiento is not None:
        movimientos.append(movimiento)
    print("Producto modificado correctamente.")


def desactivar_producto(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    producto = buscar_producto(productos, pedir_codigo())
    if producto is None:
        print("No existe un producto con ese código.")
        return
    if not producto["activo"]:
        print("El producto ya está inactivo.")
        return

    mostrar_producto(producto)
    while True:
        respuesta = input("¿Desactivar el producto? (S/N): ").strip().upper()
        if respuesta == "S":
            producto["activo"] = False
            print("Producto desactivado correctamente.")
            return
        if respuesta == "N":
            print("Desactivación cancelada.")
            return
        print("Respuesta inválida. Ingresá S o N.")


def menu_productos(productos, movimientos=None):
    while True:
        print("\nGestión de productos")
        print("1. Registrar producto.")
        print("2. Consultar por código.")
        print("3. Listar productos.")
        print("4. Modificar producto.")
        print("5. Desactivar producto.")
        print("6. Volver al menú principal.")
        opcion = input("Seleccioná una opción: ").strip()
        if opcion == "1":
            registrar_producto(productos, movimientos)
        elif opcion == "2":
            consultar_producto(productos)
        elif opcion == "3":
            listar_productos(productos)
        elif opcion == "4":
            modificar_producto(productos, movimientos)
        elif opcion == "5":
            desactivar_producto(productos)
        elif opcion == "6":
            break
        else:
            print("Opción incorrecta. Ingresá un número del 1 al 6.")

