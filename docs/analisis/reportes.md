# Reportes y estadísticas en memoria

Los reportes usan los productos y las ventas que están en memoria. Ver [diagramas](../diagramas/README.md) y [pseudocódigo](../pseint/README.md).

| Proceso | Objetivo y entradas | Procesamiento | Salidas |
| --- | --- | --- | --- |
| Listado general | Revisar todos los productos del catálogo. | Mostrar la lista de productos sin cambiar sus datos. | Fichas, incluidos inactivos, o aviso de catálogo vacío. |
| Stock mínimo | Detectar productos en el límite o por debajo. | Seleccionar `existencia <= stock_minimo`; incluir inactivos del inventario físico. | Productos y cantidades, o aviso sin coincidencias. |
| Historial de ventas | Consultar ventas confirmadas de la sesión. | Recorrer ventas y mostrar fecha, número, detalle, subtotal, IVA y total históricos. | Historial ordenado o aviso sin ventas. |
| Total de ingresos | Conocer el ingreso por ventas confirmadas. | Sumar los totales de venta, incluido el IVA; redondear a dos decimales. | Total de ingresos, cero si no hay ventas. |
| Producto más vendido | Identificar unidades vendidas por código. | Acumular cantidades de cada detalle de venta; calcular el máximo y mostrar todos los empates. Usar el nombre de su primera aparición en el historial. | Código, nombre guardado en la venta y unidades, o un aviso si no hay ventas. |
| Valor del inventario | Calcular el valor de venta del stock actual. | Multiplicar cada existencia por su precio unitario redondeado a dos decimales, redondear los importes y sumarlos. Incluir productos inactivos, pues siguen en inventario físico. | Valor total o aviso de importe fuera de rango. No es el costo ni la ganancia. |
| Promedio por período | Medir ventas e ingresos por día entre dos fechas, contando el primer y el último día. | Validar fechas YYYY-MM-DD y fin no anterior al inicio; filtrar ventas por su fecha de Guatemala; contar días calendario, incluidos días sin ventas; dividir número de ventas e ingresos por días. | Cantidad de ventas, días, ingresos y promedios diarios de ventas e ingresos; ceros si no hay coincidencias. |

## Reglas y validaciones compartidas

- Ningún reporte modifica productos, ventas ni movimientos.
- Las ventas canceladas no existen en la lista y no participan en resultados.
- Para las ventas anteriores se usan los precios y totales que tenían al confirmarse, aunque después cambie el precio del producto.
- Aceptar un período de un solo día y fechas válidas sin ventas; rechazar formatos incorrectos, fechas imposibles y fin anterior al inicio. Enter en una fecha cancela el reporte para volver al submenú.
- Rechazar sumas o productos cuyo resultado no sea finito o cuya conversión exceda el rango numérico; mostrar un aviso en lugar de infinito o una excepción.
- No dividir por cero: un período válido cuenta al menos un día porque incluye la fecha inicial y la final.
- El número de unidades es una suma de enteros, no el número de líneas del detalle.

## Navegación

Opción 4 del menú principal: submenú con los siete reportes y opción 8 para volver. Después de cada reporte se vuelve al submenú. Una opción inválida muestra un aviso y no termina el programa.

**Diagramas de los procesos:** [consultar imágenes](../diagramas/README.md).
