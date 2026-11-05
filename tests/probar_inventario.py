"""Ejecutar: python3 tests/probar_inventario.py."""

import io
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import inventario
import productos as modulo_productos
from ventas import registrar_venta


def catalogo():
    return [{"codigo": "P1", "nombre": "Cuaderno", "categoria": "Útiles", "precio": 10.0,
             "existencia": 3, "stock_minimo": 1, "activo": True}]


def ejecutar(funcion, argumentos, entradas):
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
        funcion(*argumentos)
    return salida.getvalue()


def probar_entrada():
    productos, movimientos = catalogo(), []
    antes = datetime.now(ZoneInfo("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")
    salida = ejecutar(inventario.registrar_entrada, [productos, movimientos], [" p1 ", "2", " Compra ", "s"])
    despues = datetime.now(ZoneInfo("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")
    assert productos[0]["existencia"] == 5 and len(movimientos) == 1
    m = movimientos[0]
    assert m["codigo"] == "P1" and m["tipo"] == "Entrada" and m["cantidad"] == 2
    assert m["descripcion"] == "Compra" and antes <= m["fecha"] <= despues
    assert "Entrada registrada correctamente" in salida


def probar_validaciones():
    productos, movimientos = catalogo(), []
    salida = ejecutar(inventario.registrar_entrada, [productos, movimientos],
                      ["", "P1", "-1", "abc", "1.5", "0", "2", "", " ", "Compra", "x", "S"])
    assert "El código es obligatorio." in salida
    assert salida.count("Cantidad de entrada: valor inválido.") == 3
    assert "La cantidad debe ser mayor que cero." in salida
    assert salida.count("La descripción es obligatoria.") == 2
    assert "Respuesta inválida." in salida
    assert productos[0]["existencia"] == 5 and len(movimientos) == 1


def probar_cancelacion_e_inexistente():
    for entradas in [["P1", "2", "Compra", "N"], ["NO-EXISTE"]]:
        productos, movimientos = catalogo(), []
        ejecutar(inventario.registrar_entrada, [productos, movimientos], entradas)
        assert productos == catalogo() and movimientos == []


def probar_vacios():
    for funcion, argumentos in [
        (inventario.registrar_entrada, [[], []]), (inventario.consultar_existencias, [[]]),
        (inventario.consultar_stock_minimo, [[]]), (inventario.consultar_movimientos, [[]]),
    ]:
        salida = ejecutar(funcion, argumentos, [])
        assert "No hay" in salida


def probar_limite_minimo():
    productos = catalogo()
    productos.extend([dict(productos[0], codigo="P2", existencia=1),
                      dict(productos[0], codigo="P3", existencia=0, activo=False)])
    bajos = inventario.productos_con_stock_minimo(productos)
    assert [p["codigo"] for p in bajos] == ["P2", "P3"]
    salida = ejecutar(inventario.consultar_stock_minimo, [productos], [])
    assert "P1 -" not in salida and "P2 -" in salida and "Estado: Inactivo" in salida
    salida = ejecutar(inventario.consultar_stock_minimo, [catalogo()], [])
    assert "No hay productos en el stock mínimo" in salida


def probar_inactivo():
    productos, movimientos = catalogo(), []
    productos[0]["activo"] = False
    ejecutar(inventario.registrar_entrada, [productos, movimientos], ["P1", "1", "Recepción", "S"])
    assert productos[0]["existencia"] == 4 and productos[0]["activo"] is False


def probar_registro_inicial():
    productos, movimientos = [], []
    ejecutar(modulo_productos.registrar_producto, [productos, movimientos],
             ["P1", "Cuaderno", "Útiles", "10", "0", "1"])
    assert len(movimientos) == 1 and movimientos[0]["tipo"] == "Entrada inicial"
    assert movimientos[0]["cantidad"] == 0 and movimientos[0]["codigo"] == "P1"


def probar_ajustes():
    productos, movimientos = catalogo(), []
    ejecutar(modulo_productos.modificar_producto, [productos, movimientos], ["P1", "", "", "", "5", ""])
    ejecutar(modulo_productos.modificar_producto, [productos, movimientos], ["P1", "", "", "", "1", ""])
    ejecutar(modulo_productos.modificar_producto, [productos, movimientos], ["P1", "Otro", "", "", "", ""])
    assert [(m["tipo"], m["cantidad"]) for m in movimientos] == [("Ajuste de entrada", 2), ("Ajuste de salida", 4)]
    assert productos[0]["existencia"] == 1


def probar_salidas_ventas():
    productos, ventas, movimientos = catalogo(), [], []
    ejecutar(registrar_venta, [productos, ventas, movimientos], ["P1", "1", "P1", "1", "", "S"])
    assert len(movimientos) == 1 and movimientos[0]["cantidad"] == 2
    assert movimientos[0]["tipo"] == "Salida por venta"
    assert movimientos[0]["descripcion"] == "Venta número 1"
    assert movimientos[0]["fecha"] == ventas[0]["fecha"]
    ejecutar(registrar_venta, [productos, ventas, movimientos], ["P1", "1", "", "N"])
    assert len(movimientos) == 1 and productos[0]["existencia"] == 1


def probar_historial():
    productos, movimientos = catalogo(), []
    ejecutar(inventario.registrar_entrada, [productos, movimientos], ["P1", "1", "Compra", "S"])
    ejecutar(inventario.registrar_entrada, [productos, movimientos], ["P1", "2", "Reposición", "S"])
    salida = ejecutar(inventario.consultar_movimientos, [movimientos], [])
    assert salida.index("Compra") < salida.index("Reposición")
    for m in movimientos:
        for dato in (m["fecha"], m["codigo"], m["tipo"], m["descripcion"]):
            assert dato in salida


def probar_lectura_interrumpida():
    productos, movimientos = catalogo(), []
    valores = iter(["P1", "2", "Compra"])
    def leer(mensaje):
        valor = next(valores, None)
        if valor is None:
            raise EOFError
        return valor
    try:
        with patch("builtins.input", side_effect=leer), redirect_stdout(io.StringIO()):
            inventario.registrar_entrada(productos, movimientos)
    except EOFError:
        pass
    else:
        raise AssertionError("Se esperaba fin de entrada")
    assert productos == catalogo() and movimientos == []


def probar_consola():
    entradas = ["1", "1", "P1", "Cuaderno", "Útiles", "10", "3", "1", "6",
                "2", "P1", "2", "", "S", "3", "x", "1", "3", "2", "P1", "2", "Compra", "S",
                "3", "4", "5", "5"]
    r = subprocess.run([sys.executable, str(Path(__file__).resolve().parents[1] / "src/main.py")],
                       input="\n".join(entradas) + "\n", text=True, capture_output=True, timeout=5)
    assert r.returncode == 0, r.stderr
    for texto in ["Entrada inicial", "Salida por venta", "Venta número 1", "Compra",
                  "No hay productos en el stock mínimo", "Entrada registrada correctamente. Cantidad disponible: 3"]:
        assert texto in r.stdout, texto
    assert "Opción incorrecta." in r.stdout


def main():
    pruebas = [probar_entrada, probar_validaciones, probar_cancelacion_e_inexistente,
               probar_vacios, probar_limite_minimo, probar_inactivo, probar_registro_inicial,
               probar_ajustes, probar_salidas_ventas, probar_historial,
               probar_lectura_interrumpida, probar_consola]
    for prueba in pruebas:
        prueba()
        print("PASS:", prueba.__name__)
    print(str(len(pruebas)) + " pruebas de inventario completadas correctamente.")


if __name__ == "__main__":
    main()
