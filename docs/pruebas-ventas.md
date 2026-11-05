# Pruebas de ventas en memoria

Los resultados generales están en [pruebas de entrega](pruebas-entrega.md).

El registro de `python3 tests/probar_ventas.py` contiene **13 pruebas aprobadas**. [Resultados](../evidencias/ventas/pruebas.txt).

| Caso | Datos | Resultado esperado | Resultado obtenido y conclusión |
| --- | --- | --- | --- |
| Venta múltiple | 2 unidades a 10 y 3 a 2.50 | Subtotal 27.50, IVA 3.30, total 30.80; existencias 3 y 0. | Valores comprobados; fecha real dentro del intervalo de ejecución. Aprobada. |
| Código repetido | P1 con 5 disponibles; agregar 2, intentar 4, aceptar 3, volver a intentar P1 | Rechazar exceso y acumular 5 en una línea; total 56.00. | Una línea y stock cero, sin sobreventa. Aprobada. |
| Cantidades incorrectas | -1, abc, 1.5, vacío, cero, 6 para stock 5; finalmente 2 | Rechazar las seis entradas y vender 2. | Mensajes y stock final 3 verificados. Aprobada. |
| Sin disponibles | Lista vacía, catálogo inactivo o stock cero | No pedir una venta ni cambiar listas. | Retorno sin venta. Aprobada. |
| Código incorrecto/inactivo/sin stock | NO, INACTIVO, VACIO y luego P2 | Rechazar tres códigos y vender P2. | Solo P2 aparece en el detalle. Aprobada. |
| Cancelación | Enter sin líneas o confirmar N después de seleccionar P1 | Conservar stock y no crear venta. | Listas originales intactas. Aprobada. |
| Confirmación y consecutivos | Cancelar; confirmar con respuestas inválidas antes de S; segunda venta | Numeración 1 y 2 sin consumir número por cancelar. | Dos avisos y números esperados. Aprobada. |
| Copia del historial | Vender P1 y después cambiar nombre y precio del catálogo | Conservar nombre, precio e importes originales. | Detalle independiente del catálogo. Aprobada. |
| Decimales y precio cero | Tres unidades a 0.10 y una gratuita | Subtotal 0.30, IVA 0.04 y total 0.34. | Importes y descuento de la unidad gratuita correctos. Aprobada. |
| Desbordamiento | Precio 1e308 por dos; cantidad 10^400 a precio 1 | Rechazar el importe, sin venta ni descuento. | Ambos intentos rechazados. Aprobada. |
| Lectura interrumpida | Fin de entrada antes de confirmar | No guardar ni descontar. | Stock intacto y lista de ventas vacía. Aprobada; el menú no captura EOF. |
| Desbordamiento tras línea válida | Agregar P2 a 2.50 y luego un importe fuera de rango en P1 | Conservar subtotal 2.50, IVA 0.30 y total 2.80. | La prueba falló en la primera ejecución y pasó tras corregir el cálculo provisional. |
| Consola completa | Registrar P1, vender 2 a 10 y consultar stock | IVA 2.40, total 22.40, venta 1 y cantidad restante 3. | Proceso real terminó con código 0 y mensajes esperados. Aprobada. |

## Error real detectado y corregido

La prueba del desbordamiento tras una línea válida produjo `AssertionError`: al rechazar un producto por un importe demasiado grande, se cambiaban los totales de los productos ya aceptados. Se corrigió guardando primero los cálculos nuevos por separado y usando esos valores solo si eran válidos. La prueba de regresión quedó en `probar_desbordamiento_con_carrito` y pasó después de la corrección.

Los resultados están guardados como salidas de consola.
