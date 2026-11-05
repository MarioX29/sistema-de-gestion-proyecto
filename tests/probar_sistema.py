"""Pruebas con la biblioteca estándar: python3 tests/probar_sistema.py."""

import io
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch


raiz = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(raiz / "src"))
import productos as sistema


def ejecutar_consola(entradas):
    resultado = subprocess.run(
        [sys.executable, str(raiz / "src/main.py")],
        input="\n".join(entradas) + "\n",
        capture_output=True,
        text=True,
        timeout=5,
    )
    assert resultado.returncode == 0, resultado.stderr
    return resultado.stdout


def registrar(productos, entradas):
    return ejecutar_operacion(sistema.registrar_producto, productos, entradas)


def ejecutar_operacion(operacion, productos, entradas):
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
        operacion(productos)
    return salida.getvalue()


def probar_salida():
    salida = ejecutar_consola(["5", "1"])
    assert salida.count("Sistema de gestión comercial") == 1
    assert "Hasta luego." in salida
    assert "Código:" not in salida


def probar_opciones_invalidas():
    salida = ejecutar_consola(["0", "6", "-1", "abc", "", "1.5", "15", "5"])
    assert salida.count("Opción incorrecta.") == 7
    assert salida.count("Sistema de gestión comercial") == 8


def probar_navegacion_modulos():
    salida = ejecutar_consola([" 2 ", "3", "5", "4", "8", " 5 "])
    assert "Control de inventario" in salida and "Reportes y estadísticas" in salida
    assert "Pendiente de desarrollar" not in salida
    assert "No hay productos activos con existencias para vender." in salida
    assert salida.count("Sistema de gestión comercial") == 4


def probar_registro_normal():
    productos = []
    salida = registrar(productos, [" p01 ", " Cuaderno ", " Útiles ", "12.50", "3", "1"])
    assert productos == [{
        "codigo": "P01", "nombre": "Cuaderno", "categoria": "Útiles",
        "precio": 12.5, "existencia": 3, "stock_minimo": 1, "activo": True,
    }]
    assert salida.count("Producto registrado correctamente.") == 1


def probar_obligatorios():
    productos = []
    salida = registrar(productos, ["", "   ", "P1", "", "  ", "Lápiz", "", "  ", "Útiles", "1", "0", "0"])
    assert salida.count("El código es obligatorio.") == 2
    assert salida.count("El nombre es obligatorio.") == 2
    assert salida.count("La categoría es obligatoria.") == 2
    assert len(productos) == 1
    assert productos[0]["existencia"] == 0


def probar_codigo_repetido():
    productos = []
    registrar(productos, ["P1", "Lápiz", "Útiles", "2", "4", "1"])
    original = productos[0].copy()
    salida = registrar(productos, [" p1 ", "P1", "P2", "Borrador", "Útiles", "1.25", "0", "2"])
    assert salida.count("El código ya está registrado.") == 2
    assert len(productos) == 2
    assert productos[0] == original
    assert productos[1]["codigo"] == "P2"


def probar_precio_invalido():
    invalidos = ["", " ", "abc", "-1", "1,5", "1.2.3", ".", "NaN", "inf", "1e3", "9" * 400]
    productos = []
    salida = registrar(productos, ["P1", "Cuaderno", "Útiles"] + invalidos + [" 2.75 ", "2", "1"])
    assert salida.count("Precio inválido.") == len(invalidos)
    assert len(productos) == 1
    assert productos[0]["precio"] == 2.75


def probar_existencia_invalida():
    invalidos = ["", " ", "abc", "-1", "1.5", "1,5", "NaN", "inf", "1e2", "²", "9" * 5000]
    productos = []
    salida = registrar(productos, ["P1", "Cuaderno", "Útiles", "1"] + invalidos + [" 0 ", "0"])
    assert salida.count("Existencia inicial: valor inválido.") == len(invalidos)
    assert len(productos) == 1
    assert productos[0]["existencia"] == 0


def probar_decimales():
    productos = []
    registrar(productos, ["P1", "A", "Útiles", ".5", "01", "0"])
    registrar(productos, ["P2", "B", "Útiles", "2.", "0", "1"])
    assert productos[0]["precio"] == 0.5
    assert productos[0]["existencia"] == 1
    assert productos[1]["precio"] == 2.0


def probar_flujo_completo():
    salida = ejecutar_consola([
        "1", "1", "p1", "Cuaderno", "Útiles", "10", "2", "1",
        "1", "P1", "P2", "Lápiz", "Útiles", "-2", "1.50", "-1", "0", "1",
        "6", "2", "", "3", "5", "4", "8", "x", "5",
    ])
    assert salida.count("Producto registrado correctamente.") == 2
    assert salida.count("El código ya está registrado.") == 1
    assert salida.count("Precio inválido.") == 1
    assert salida.count("Existencia inicial: valor inválido.") == 1
    assert "Pendiente de desarrollar" not in salida
    assert "Venta cancelada. No se agregaron productos." in salida
    assert salida.count("Opción incorrecta.") == 1
    assert salida.count("Sistema de gestión comercial") == 6


def probar_sin_persistencia():
    entradas = ["1", "1", "P1", "Lápiz", "Útiles", "1", "0", "0", "6", "5"]
    for intento in range(2):
        salida = ejecutar_consola(entradas)
        assert "El código ya está registrado." not in salida
        assert salida.count("Producto registrado correctamente.") == 1


def catalogo():
    return [{
        "codigo": "P1", "nombre": "Cuaderno", "categoria": "Útiles",
        "precio": 12.5, "existencia": 3, "stock_minimo": 1, "activo": True,
    }]


def probar_ceros_y_minimo_superior():
    productos = []
    registrar(productos, ["P1", "Muestra", "Promoción", "0", "0", "5"])
    assert productos[0]["precio"] == 0
    assert productos[0]["existencia"] == 0
    assert productos[0]["stock_minimo"] == 5


def probar_stock_minimo_invalido():
    productos = []
    invalidos = ["", "-1", "1.5", "abc", "NaN", "1e3", "9" * 5000]
    salida = registrar(productos, ["P1", "Cuaderno", "Útiles", "1", "0"] + invalidos + ["2"])
    assert salida.count("Stock mínimo: valor inválido.") == len(invalidos)
    assert len(productos) == 1
    assert productos[0]["stock_minimo"] == 2


def probar_consulta():
    productos = catalogo()
    original = productos[0].copy()
    salida = ejecutar_operacion(sistema.consultar_producto, productos, ["", " p1 "])
    assert "El código es obligatorio." in salida
    for dato in ["Código: P1", "Nombre: Cuaderno", "Categoría: Útiles", "Precio: 12.50",
                 "Cantidad disponible: 3", "Stock mínimo: 1", "Estado: Activo"]:
        assert dato in salida, dato
    assert productos == [original]


def probar_productos_inexistentes():
    for operacion in [sistema.consultar_producto, sistema.modificar_producto, sistema.desactivar_producto]:
        productos = catalogo()
        original = productos[0].copy()
        salida = ejecutar_operacion(operacion, productos, ["NO-EXISTE"])
        assert "No existe un producto con ese código." in salida
        assert productos == [original]


def probar_catalogo_vacio():
    for operacion in [sistema.consultar_producto, sistema.listar_productos,
                      sistema.modificar_producto, sistema.desactivar_producto]:
        productos = []
        salida = ejecutar_operacion(operacion, productos, [])
        assert "No hay productos registrados." in salida
        assert productos == []


def probar_listado():
    productos = catalogo()
    segundo = productos[0].copy()
    segundo["codigo"] = "P2"
    segundo["activo"] = False
    productos.append(segundo)
    originales = [producto.copy() for producto in productos]
    salida = ejecutar_operacion(sistema.listar_productos, productos, [])
    assert salida.index("Código: P1") < salida.index("Código: P2")
    assert "Estado: Activo" in salida and "Estado: Inactivo" in salida
    assert salida.count("Stock mínimo: 1") == 2
    assert productos == originales


def probar_modificacion():
    productos = catalogo()
    otro = productos[0].copy()
    otro["codigo"] = "P2"
    original_otro = otro.copy()
    productos.append(otro)
    salida = ejecutar_operacion(sistema.modificar_producto, productos,
                               [" p1 ", " Libreta ", " Oficina ", "0", "0", "2"])
    assert "Producto modificado correctamente." in salida
    assert productos[0] == {
        "codigo": "P1", "nombre": "Libreta", "categoria": "Oficina",
        "precio": 0.0, "existencia": 0, "stock_minimo": 2, "activo": True,
    }
    assert productos[1] == original_otro
    assert len(productos) == 2
    original_editado = productos[0].copy()
    salida = ejecutar_operacion(sistema.modificar_producto, productos, ["P1", "", "", "", "", ""])
    assert "No se realizaron cambios." in salida
    assert productos[0] == original_editado


def probar_modificacion_conservar():
    productos = catalogo()
    productos[0]["activo"] = False
    original = productos[0].copy()
    salida = ejecutar_operacion(sistema.modificar_producto, productos, ["P1", "", " ", "", "", ""])
    assert "No se realizaron cambios." in salida
    assert productos == [original]
    salida = ejecutar_operacion(sistema.modificar_producto, productos, ["P1", "Nuevo", "", "", "", ""])
    assert "Producto modificado correctamente." in salida
    assert productos[0]["nombre"] == "Nuevo"
    assert productos[0]["activo"] is False


def probar_modificacion_invalida():
    productos = catalogo()
    salida = ejecutar_operacion(sistema.modificar_producto, productos,
                               ["P1", "Nuevo", "Oficina", "-1", "NaN", "abc", "1.25",
                                "-2", "2.5", "5", "-1", "xyz", "0"])
    assert salida.count("Precio inválido.") == 3
    assert salida.count("Cantidad disponible: valor inválido.") == 2
    assert salida.count("Stock mínimo: valor inválido.") == 2
    assert productos[0]["precio"] == 1.25
    assert productos[0]["existencia"] == 5
    assert productos[0]["stock_minimo"] == 0


def probar_lectura_interrumpida():
    for operacion, entradas in [
        (sistema.registrar_producto, ["P2", "Nuevo", "Oficina", "1", "2"]),
        (sistema.modificar_producto, ["P1", "Nuevo", "Oficina", "1", "2"]),
    ]:
        productos = catalogo()
        original = productos[0].copy()
        salida = io.StringIO()
        def entrada(mensaje):
            if entradas:
                return entradas.pop(0)
            raise EOFError
        try:
            with patch("builtins.input", side_effect=entrada), redirect_stdout(salida):
                operacion(productos)
        except EOFError:
            pass
        else:
            raise AssertionError("Se esperaba fin de entrada antes del stock mínimo")
        assert productos == [original]


def probar_desactivacion():
    productos = catalogo()
    original = productos[0].copy()
    salida = ejecutar_operacion(sistema.desactivar_producto, productos, ["p1", "", "sí", " s "])
    assert salida.count("Respuesta inválida.") == 2
    assert "Producto desactivado correctamente." in salida
    original["activo"] = False
    assert productos == [original]
    salida = ejecutar_operacion(sistema.desactivar_producto, productos, ["P1"])
    assert "El producto ya está inactivo." in salida
    assert productos == [original]


def probar_cancelar_desactivacion():
    productos = catalogo()
    original = productos[0].copy()
    salida = ejecutar_operacion(sistema.desactivar_producto, productos, ["P1", " n "])
    assert "Desactivación cancelada." in salida
    assert productos == [original]


def probar_codigo_inactivo():
    productos = catalogo()
    productos[0]["activo"] = False
    original = productos[0].copy()
    salida = registrar(productos, [" p1 ", "P2", "Lápiz", "Útiles", "1", "2", "0"])
    assert salida.count("El código ya está registrado.") == 1
    assert productos[0] == original
    assert len(productos) == 2
    salida = ejecutar_operacion(sistema.consultar_producto, productos, ["P1"])
    assert "Estado: Inactivo" in salida


def probar_submenu_y_operaciones():
    salida = ejecutar_consola([
        "1", "0", "7", "abc", "", "2", "3", "4", "5",
        "1", "p1", "Cuaderno", "Útiles", "12.5", "3", "1",
        "2", "NO-EXISTE", "2", "p1", "3",
        "4", "P1", "Libreta", "Oficina", "0", "0", "2",
        "5", "P1", "N", "5", "P1", "S", "2", "P1",
        "6", "1", "3", "6", "5",
    ])
    assert salida.count("Opción incorrecta. Ingresá un número del 1 al 6.") == 4
    assert salida.count("No hay productos registrados.") == 4
    assert salida.count("Producto registrado correctamente.") == 1
    assert salida.count("No existe un producto con ese código.") == 1
    assert salida.count("Producto modificado correctamente.") == 1
    assert salida.count("Desactivación cancelada.") == 1
    assert salida.count("Producto desactivado correctamente.") == 1
    assert salida.count("Estado: Inactivo") == 2
    assert "Nombre: Libreta" in salida and "Categoría: Oficina" in salida
    assert "Precio: 0.00" in salida and "Cantidad disponible: 0" in salida
    assert salida.count("Hasta luego.") == 1


def main():
    pruebas = [
        probar_salida, probar_opciones_invalidas, probar_navegacion_modulos,
        probar_registro_normal, probar_obligatorios, probar_codigo_repetido,
        probar_precio_invalido, probar_existencia_invalida, probar_decimales,
        probar_flujo_completo, probar_sin_persistencia,
        probar_ceros_y_minimo_superior, probar_stock_minimo_invalido,
        probar_consulta, probar_productos_inexistentes, probar_catalogo_vacio,
        probar_listado, probar_modificacion, probar_modificacion_conservar,
        probar_modificacion_invalida, probar_lectura_interrumpida,
        probar_desactivacion, probar_cancelar_desactivacion,
        probar_codigo_inactivo, probar_submenu_y_operaciones,
    ]
    for prueba in pruebas:
        prueba()
        print("PASS:", prueba.__name__)
    print(str(len(pruebas)) + " pruebas completadas correctamente.")


if __name__ == "__main__":
    main()
