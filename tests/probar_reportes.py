"""Datos sintéticos para pruebas; no son ventas reales del proyecto."""

from contextlib import redirect_stdout
from copy import deepcopy
from datetime import date
import io
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import reportes


def ventas_ejemplo():
    return [
        {"numero": 1, "fecha": "2026-01-01 10:00:00", "subtotal": 20, "iva": 2.4, "total": 22.4,
         "detalle": [{"codigo": "P1", "nombre": "Cuaderno", "precio_unitario": 10,
                      "cantidad": 2, "subtotal": 20}]},
        {"numero": 2, "fecha": "2026-01-03 12:00:00", "subtotal": 5, "iva": 0.6, "total": 5.6,
         "detalle": [{"codigo": "P2", "nombre": "Lápiz", "precio_unitario": 2.5,
                      "cantidad": 2, "subtotal": 5}]},
    ]


def productos_ejemplo():
    return [
        {"codigo": "P1", "nombre": "Cuaderno", "categoria": "Útiles", "precio": 10,
         "existencia": 3, "stock_minimo": 3, "activo": True},
        {"codigo": "P2", "nombre": "Lápiz", "categoria": "Útiles", "precio": 2.5,
         "existencia": 1, "stock_minimo": 2, "activo": False},
    ]


def ejecutar(funcion, argumentos, entradas=()):
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
        funcion(*argumentos)
    return salida.getvalue()


def probar_ingresos():
    assert reportes.total_ingresos(ventas_ejemplo()) == 28.0
    assert reportes.total_ingresos([]) == 0
    salida = ejecutar(reportes.reporte_ingresos, [ventas_ejemplo()])
    assert "incluye IVA): 28.00" in salida


def probar_empate_y_acumulacion():
    ventas = ventas_ejemplo()
    assert [p["codigo"] for p in reportes.productos_mas_vendidos(ventas)] == ["P1", "P2"]
    ventas.append(deepcopy(ventas[0]))
    ganadores = reportes.productos_mas_vendidos(ventas)
    assert len(ganadores) == 1 and ganadores[0]["codigo"] == "P1"
    assert ganadores[0]["cantidad"] == 4
    salida = ejecutar(reportes.reporte_mas_vendido, [ventas_ejemplo()])
    assert "P1 - Cuaderno | Unidades: 2" in salida and "P2 - Lápiz | Unidades: 2" in salida


def probar_valor_inactivos():
    productos = productos_ejemplo()
    assert reportes.valor_inventario(productos) == 32.5
    salida = ejecutar(reportes.reporte_valor_inventario, [productos])
    assert "incluye inactivos): 32.50" in salida
    productos[0]["precio"] = 0.1
    assert reportes.valor_inventario(productos) == 2.8


def probar_historial():
    salida = ejecutar(reportes.historial_ventas, [ventas_ejemplo()])
    assert salida.index("Venta número: 1") < salida.index("Venta número: 2")
    assert "2026-01-01 10:00:00" in salida and "Total: 22.40" in salida


def probar_periodo_inclusivo():
    resumen = reportes.resumen_periodo(ventas_ejemplo(), date(2026, 1, 1), date(2026, 1, 3))
    assert resumen["ventas"] == 2 and resumen["dias"] == 3 and resumen["ingresos"] == 28.0
    assert resumen["promedio_ventas"] == 2 / 3 and resumen["promedio_ingresos"] == 9.33
    un_dia = reportes.resumen_periodo(ventas_ejemplo(), date(2026, 1, 3), date(2026, 1, 3))
    assert un_dia["ventas"] == 1 and un_dia["dias"] == 1 and un_dia["promedio_ingresos"] == 5.6


def probar_periodo_sin_ventas():
    resumen = reportes.resumen_periodo(ventas_ejemplo(), date(2026, 2, 1), date(2026, 2, 2))
    assert resumen == {"ventas": 0, "dias": 2, "ingresos": 0.0,
                       "promedio_ventas": 0.0, "promedio_ingresos": 0.0}


def probar_fechas_invalidas():
    salida = ejecutar(reportes.reporte_promedio, [ventas_ejemplo()],
                      ["abc", "2026-02-30", "2026-1-1", "2026-01-01", "2025-12-31", "2026-01-03"])
    assert salida.count("Fecha inválida.") == 3
    assert "La fecha final no puede ser anterior" in salida
    assert "Ventas del período: 2" in salida and "Promedio de ingresos por día: 9.33" in salida


def probar_cancelacion():
    for entradas in [[""], ["2026-01-01", ""]]:
        salida = ejecutar(reportes.reporte_promedio, [ventas_ejemplo()], entradas)
        assert "Reporte cancelado." in salida


def probar_vacios():
    assert reportes.productos_mas_vendidos([]) == []
    assert reportes.valor_inventario([]) == 0
    for funcion in [reportes.historial_ventas, reportes.reporte_mas_vendido]:
        assert "No hay ventas registradas." in ejecutar(funcion, [[]])
    assert "0.00" in ejecutar(reportes.reporte_ingresos, [[]])
    assert "0.00" in ejecutar(reportes.reporte_valor_inventario, [[]])


def probar_desbordamientos():
    productos = productos_ejemplo()
    productos[0]["precio"] = 1e308
    assert reportes.valor_inventario(productos) is None
    assert "excede el rango" in ejecutar(reportes.reporte_valor_inventario, [productos])
    productos[0]["precio"] = 1
    productos[0]["existencia"] = 10 ** 400
    assert reportes.valor_inventario(productos) is None
    ventas = ventas_ejemplo()
    for venta in ventas:
        venta["total"] = 1e308
    assert reportes.total_ingresos(ventas) is None
    assert "excede el rango" in ejecutar(reportes.reporte_ingresos, [ventas])
    assert "excede el rango" in ejecutar(reportes.reporte_promedio, [ventas], ["2026-01-01", "2026-01-03"])


def probar_sin_modificar():
    productos, ventas = productos_ejemplo(), ventas_ejemplo()
    originales = deepcopy([productos, ventas])
    ejecutar(reportes.menu_reportes, [productos, ventas],
             ["1", "2", "3", "4", "5", "6", "7", "2026-01-01", "2026-01-03", "8"])
    assert [productos, ventas] == originales


def probar_consola_completa():
    entradas = ["1", "1", "P1", "Cuaderno", "Útiles", "10", "5", "3", "6",
                "2", "P1", "2", "", "S", "4", "x", "1", "2", "3", "4", "5", "6",
                "7", "", "8", "5"]
    r = subprocess.run([sys.executable, str(Path(__file__).resolve().parents[1] / "src/main.py")],
                       input="\n".join(entradas) + "\n", text=True, capture_output=True, timeout=5)
    assert r.returncode == 0, r.stderr
    for texto in ["Total de ingresos por ventas (incluye IVA): 22.40", "Unidades: 2",
                  "Valor del inventario a precio de venta (incluye inactivos): 30.00",
                  "Reporte cancelado.", "Opción incorrecta. Ingresá un número del 1 al 8."]:
        assert texto in r.stdout, texto


def main():
    pruebas = [probar_ingresos, probar_empate_y_acumulacion, probar_valor_inactivos,
               probar_historial, probar_periodo_inclusivo, probar_periodo_sin_ventas,
               probar_fechas_invalidas, probar_cancelacion, probar_vacios,
               probar_desbordamientos, probar_sin_modificar, probar_consola_completa]
    for prueba in pruebas:
        prueba()
        print("PASS:", prueba.__name__)
    print(str(len(pruebas)) + " pruebas de reportes completadas correctamente.")


if __name__ == "__main__":
    main()
