# Pruebas de reportes

- `pruebas-completas.txt`: resultados de las 62 pruebas de Python.
- `entradas.txt`: datos utilizados para probar los reportes.
- `salida.txt`: resultados del programa.

El caso registra Cuaderno, con 5 unidades a 10.00, y Lápiz, con 3 unidades a 2.50. Después vende 2 cuadernos y 1 lápiz, registra una entrada de 1 cuaderno y consulta los reportes.

| Resultado | Valor |
| --- | --- |
| Ingresos | 25.20 |
| Producto más vendido | P1, 2 unidades |
| Valor del inventario | 45.00 |
| Ventas del día | 1 |
| Promedio de ingresos del día | 25.20 |

## Ejecución

```bash
python3 tests/probar_todo.py
python3 src/main.py < evidencias/reportes/entradas.txt
```

Las dos fechas finales de `entradas.txt` deben coincidir con la fecha de ejecución para incluir la venta en el reporte del día.

Los archivos contienen registros de las pruebas. El programa mantiene sus datos en memoria durante la sesión.
