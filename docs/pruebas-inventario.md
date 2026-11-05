# Pruebas de inventario

Los resultados generales están en [pruebas de entrega](pruebas-entrega.md).

Se ejecutó `python3 tests/probar_inventario.py`: **12 pruebas aprobadas**. También pasaron las 25 de productos y las 13 de ventas, para un total de 50. [Salida real](../evidencias/inventario/pruebas.txt).

| Caso | Datos | Resultado esperado | Resultado obtenido y conclusión |
| --- | --- | --- | --- |
| Entrada válida | Stock 3, entrada 2, descripción Compra | Stock 5 y movimiento con fecha real, código, tipo, cantidad y descripción. | Campos y fecha dentro del intervalo real de ejecución comprobados. Aprobada. |
| Validaciones | Código vacío; cantidades -1, abc, 1.5, 0; descripción vacía; confirmación x | Repetir datos incorrectos y guardar solo la entrada válida. | Avisos esperados y un solo movimiento. Aprobada. |
| Cancelación/inexistente | Confirmar N o código NO-EXISTE | No cambiar stock ni historial. | Estructuras intactas. Aprobada. |
| Listas vacías | Entrada, existencias, mínimos e historial vacíos | Informar sin fallar. | Cuatro retornos correctos. Aprobada. |
| Límite de mínimo | Stocks 3, 1 y 0 con mínimo 1 | Incluir los de 1 y 0, incluido el inactivo. | Códigos y estados correctos; aviso si no hay alertas. Aprobada. |
| Recepción de inactivo | Producto inactivo con 3, entrada 1 | Aumentar a 4 sin reactivar. | Cantidad y estado correctos. Aprobada. |
| Registro inicial | Nuevo producto con existencia 0 | Registrar Entrada inicial con cantidad 0. | Movimiento completo y código correcto. Aprobada. |
| Ajustes | Cambiar existencia 3 a 5, luego a 1 y después solo el nombre | Ajuste de entrada 2, salida 4 y sin movimiento por nombre. | Dos movimientos con cantidades positivas. Aprobada. |
| Venta integrada | Agregar dos veces P1, confirmar; luego cancelar otra venta | Una salida por 2 con fecha y número de venta; ninguna salida por cancelación. | Historial y stock comprobados. Aprobada. |
| Consulta de historial | Entradas Compra y Reposición | Mostrar campos en orden de registro. | Orden y campos correctos. Aprobada. |
| Lectura interrumpida | Fin de entrada antes de confirmar | Conservar stock e historial. | Sin cambios. Aprobada. |
| Consola integrada | Registro, venta, entrada, alertas e historial; opción inválida | Mantener navegación y mostrar los tres tipos de movimientos. | Proceso terminó con código 0 y datos esperados. Aprobada. |

Las 12 pruebas de inventario pasaron. Las salidas están guardadas como registros de texto.
