# Pruebas de reportes y estadísticas

Los resultados generales están en [pruebas de entrega](pruebas-entrega.md).

Se ejecutó `python3 tests/probar_reportes.py`: **12 pruebas aprobadas**. La suite completa contiene 25 pruebas de productos/menú, 13 de ventas, 12 de inventario y 12 de reportes: **62 aprobadas**. El ejecutor `python3 tests/probar_todo.py` conserva los códigos de salida y se detiene si falla una suite.

Las fechas 2026-01-01 y 2026-01-03 son fechas de ejemplo para probar los cálculos. No corresponden a ventas reales. Las ventas creadas por el programa usan la fecha real de ejecución.

| Caso | Datos | Resultado esperado | Resultado obtenido y conclusión |
| --- | --- | --- | --- |
| Ingresos | Totales 22.40 y 5.60 | 28.00, incluido IVA; lista vacía da cero. | Suma y texto correctos. Aprobada. |
| Más vendido | P1 con 2 y P2 con 2; después otras 2 a P1 | Empate inicial y luego P1 con 4. | Ambos resultados comprobados. Aprobada. |
| Valor e inactivos | P1: 3 a 10; P2 inactivo: 1 a 2.50 | 32.50, incluyendo inactivo; con precio 0.10 en P1, 2.80. | Ambos importes correctos. Aprobada. |
| Historial | Dos ventas con detalle e importes | Mostrar en orden, con fecha y totales guardados. | Orden y campos correctos. Aprobada. |
| Período inclusive | Ventas el 1 y el 3 de enero; período de tres días | 2 ventas, 3 días, ingresos 28, 2/3 ventas diarias, 9.33 ingresos diarios. | Resultados correctos; también se probó un solo día. Aprobada. |
| Sin ventas en período | Dos días de febrero sin coincidencias | Cero ventas e ingresos y dos días. | Resumen y promedios cero. Aprobada. |
| Fechas incorrectas | abc, 2026-02-30, 2026-1-1; fin anterior al inicio | Rechazar formatos, fecha imposible y rango invertido. | Reintentos y posterior promedio correctos. Aprobada. |
| Cancelación | Enter al inicio o al solicitar fin | Regresar sin calcular. | Cancelación en ambos casos. Aprobada. |
| Estructuras vacías | Sin productos ni ventas | Avisos o cero, sin errores. | Resultados correctos. Aprobada. |
| Desbordamientos | Precio 1e308, cantidad 10^400 o suma de dos totales 1e308 | Error de rango sin infinito ni excepción. | Valor, ingresos y promedio protegidos. Aprobada. |
| Sin modificaciones | Ejecutar los siete reportes | Conservar productos y ventas exactamente. | Comparación profunda sin diferencias. Aprobada. |
| Consola integrada | Registrar, vender y consultar reportes; opción x y cancelación | Ingresos 22.40, producto con 2 unidades, inventario 30.00 y navegación correcta. | Proceso real terminó con código 0 y valores esperados. Aprobada. |

Las pruebas de reportes pasaron sin fallos. La [salida completa](../evidencias/reportes/pruebas-completas.txt) y la [transcripción integrada](../evidencias/reportes/README.md) documentan ejecuciones reales. Las evidencias son registros de texto.
