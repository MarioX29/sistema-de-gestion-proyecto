# Pruebas del sistema

Las pruebas revisan los datos que recibe el programa, las operaciones de cada módulo y la navegación por consola.

| Módulo | Cantidad | Casos |
| --- | --- | --- |
| Productos y menú | 25 | Registro, consulta, cambios, desactivación y validaciones. |
| Ventas | 13 | Cantidades, stock, IVA, confirmación y cancelación. |
| Inventario | 12 | Entradas, ajustes, mínimos y movimientos. |
| Reportes | 12 | Ingresos, unidades vendidas, inventario y promedios. |
| Total | 62 | Todas aprobadas en el registro de resultados. |

## Ejecución

Desde la carpeta del proyecto:

```bash
python3 tests/probar_todo.py
```

El ejecutor se detiene si falla uno de los módulos.

## Resultados por módulo

- [Productos](pruebas-productos.md)
- [Ventas](pruebas-ventas.md)
- [Inventario](pruebas-inventario.md)
- [Reportes](pruebas-reportes.md)

Los documentos por módulo describen los casos y sus resultados. El [resumen de entrega](pruebas-entrega.md) reúne los resultados de Python y PSeInt.

## Evidencias

La salida de las 62 pruebas está en [python-pruebas.txt](../evidencias/entrega/python-pruebas.txt). Los casos de PSeInt y sus resultados están en [evidencias/entrega/pseint](../evidencias/entrega/pseint/).

Las evidencias disponibles son registros de texto. Las capturas de pantalla aún no están incorporadas.
