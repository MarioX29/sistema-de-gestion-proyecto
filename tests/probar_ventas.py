"""Ejecutar: python3 tests/probar_ventas.py."""

import io
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ventas import registrar_venta


def catalogo():
    return [
        {"codigo": "P1", "nombre": "Cuaderno", "categoria": "Útiles", "precio": 10.0,
         "existencia": 5, "stock_minimo": 1, "activo": True},
        {"codigo": "P2", "nombre": "Lápiz", "categoria": "Útiles", "precio": 2.5,
         "existencia": 3, "stock_minimo": 1, "activo": True},
    ]


def ejecutar(productos, ventas, entradas):
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
        registrar_venta(productos, ventas)
    return salida.getvalue()


def probar_venta_multiple():
    productos, ventas = catalogo(), []
    antes = datetime.now(ZoneInfo("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")
    salida = ejecutar(productos, ventas, [" p1 ", "2", "P2", "3", "", " s "])
    despues = datetime.now(ZoneInfo("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")
    assert len(ventas) == 1 and ventas[0]["numero"] == 1
    assert ventas[0]["subtotal"] == 27.5 and ventas[0]["iva"] == 3.3
    assert ventas[0]["total"] == 30.8
    assert antes <= ventas[0]["fecha"] <= despues
    assert [p["existencia"] for p in productos] == [3, 0]
    assert "Total: 30.80" in salida


def probar_repetidos_y_stock():
    productos, ventas = catalogo(), []
    salida = ejecutar(productos, ventas, ["P1", "2", "P1", "4", "3", "P1", "", "S"])
    assert "Inventario insuficiente" in salida
    assert "No hay más existencias" in salida
    assert len(ventas[0]["detalle"]) == 1
    assert ventas[0]["detalle"][0]["cantidad"] == 5
    assert ventas[0]["total"] == 56.0 and productos[0]["existencia"] == 0


def probar_cantidades_invalidas():
    productos, ventas = catalogo(), []
    salida = ejecutar(productos, ventas, ["P1", "-1", "abc", "1.5", "", "0", "6", "2", "", "S"])
    assert salida.count("Cantidad a vender: valor inválido.") == 4
    assert "La cantidad debe ser mayor que cero." in salida
    assert "Inventario insuficiente" in salida
    assert productos[0]["existencia"] == 3


def probar_no_disponibles():
    for productos in [[], [dict(catalogo()[0], activo=False)], [dict(catalogo()[0], existencia=0)]]:
        ventas = []
        salida = ejecutar(productos, ventas, [])
        assert "No hay productos activos con existencias" in salida
        assert ventas == []


def probar_codigos_invalidos():
    productos, ventas = catalogo(), []
    productos.append(dict(productos[0], codigo="INACTIVO", activo=False))
    productos.append(dict(productos[0], codigo="VACIO", existencia=0))
    salida = ejecutar(productos, ventas, ["NO", "INACTIVO", "VACIO", "P2", "1", "", "S"])
    assert "No existe un producto" in salida and "El producto está inactivo." in salida
    assert "No hay más existencias" in salida
    assert len(ventas) == 1 and ventas[0]["detalle"][0]["codigo"] == "P2"


def probar_cancelaciones():
    for entradas in [[""], ["P1", "2", "", "N"]]:
        productos, ventas = catalogo(), []
        originales = [p.copy() for p in productos]
        salida = ejecutar(productos, ventas, entradas)
        assert "Venta cancelada" in salida
        assert productos == originales and ventas == []


def probar_confirmacion_y_numeracion():
    productos, ventas = catalogo(), []
    ejecutar(productos, ventas, ["P1", "1", "", "N"])
    salida = ejecutar(productos, ventas, ["P1", "1", "", "", "sí", "s"])
    ejecutar(productos, ventas, ["P2", "1", "", "S"])
    assert salida.count("Respuesta inválida.") == 2
    assert [v["numero"] for v in ventas] == [1, 2]
    assert productos[0]["existencia"] == 4


def probar_historial_independiente():
    productos, ventas = catalogo(), []
    ejecutar(productos, ventas, ["P1", "2", "", "S"])
    productos[0]["precio"] = 99
    productos[0]["nombre"] = "Editado"
    item = ventas[0]["detalle"][0]
    assert item["nombre"] == "Cuaderno" and item["precio_unitario"] == 10.0
    assert item["subtotal"] == 20.0 and ventas[0]["total"] == 22.4


def probar_redondeo_y_gratis():
    productos, ventas = catalogo(), []
    productos[0]["precio"] = 0.1
    productos[1]["precio"] = 0
    ejecutar(productos, ventas, ["P1", "3", "P2", "1", "", "S"])
    assert ventas[0]["subtotal"] == 0.3 and ventas[0]["iva"] == 0.04
    assert ventas[0]["total"] == 0.34
    assert productos[1]["existencia"] == 2


def probar_desbordamiento():
    productos, ventas = catalogo(), []
    productos[0]["precio"] = 1e308
    salida = ejecutar(productos, ventas, ["P1", "2", "",])
    assert "El importe excede el rango numérico" in salida
    assert productos[0]["existencia"] == 5 and ventas == []
    productos[0]["precio"] = 1
    productos[0]["existencia"] = 10 ** 400
    salida = ejecutar(productos, ventas, ["P1", str(10 ** 400), ""])
    assert "El importe excede el rango numérico" in salida
    assert productos[0]["existencia"] == 10 ** 400 and ventas == []


def probar_lectura_interrumpida():
    productos, ventas = catalogo(), []
    entradas = iter(["P1", "2", ""])
    def leer(mensaje):
        valor = next(entradas, None)
        if valor is None:
            raise EOFError
        return valor
    try:
        with patch("builtins.input", side_effect=leer), redirect_stdout(io.StringIO()):
            registrar_venta(productos, ventas)
    except EOFError:
        pass
    else:
        raise AssertionError("Se esperaba EOFError antes de confirmar")
    assert productos == catalogo() and ventas == []


def probar_desbordamiento_con_carrito():
    productos, ventas = catalogo(), []
    productos[0]["precio"] = 1e308
    salida = ejecutar(productos, ventas, ["P2", "1", "P1", "2", "", "S"])
    assert "El importe excede el rango numérico" in salida
    assert ventas[0]["subtotal"] == 2.5 and ventas[0]["iva"] == 0.3
    assert ventas[0]["total"] == 2.8
    assert len(ventas[0]["detalle"]) == 1
    assert productos[0]["existencia"] == 5 and productos[1]["existencia"] == 2


def probar_consola():
    entradas = ["1", "1", "P1", "Cuaderno", "Útiles", "10", "5", "1", "6",
                "2", "P1", "2", "", "S", "1", "2", "P1", "6", "5"]
    resultado = subprocess.run([sys.executable, str(Path(__file__).resolve().parents[1] / "src/main.py")],
                              input="\n".join(entradas) + "\n", capture_output=True, text=True, timeout=5)
    assert resultado.returncode == 0, resultado.stderr
    assert "IVA (12 %): 2.40" in resultado.stdout and "Total: 22.40" in resultado.stdout
    assert "Cantidad disponible: 3" in resultado.stdout
    assert "Venta registrada correctamente. Número: 1" in resultado.stdout


def main():
    pruebas = [probar_venta_multiple, probar_repetidos_y_stock, probar_cantidades_invalidas,
               probar_no_disponibles, probar_codigos_invalidos, probar_cancelaciones,
               probar_confirmacion_y_numeracion, probar_historial_independiente,
               probar_redondeo_y_gratis, probar_desbordamiento, probar_lectura_interrumpida,
               probar_desbordamiento_con_carrito,
               probar_consola]
    for prueba in pruebas:
        prueba()
        print("PASS:", prueba.__name__)
    print(str(len(pruebas)) + " pruebas de ventas completadas correctamente.")


if __name__ == "__main__":
    main()
