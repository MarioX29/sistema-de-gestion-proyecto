# Control de inventario en memoria

Aquí se explica cómo consultar y cambiar las cantidades del inventario. Ver [diagramas](../diagramas/README.md) y [pseudocódigo](../pseint/README.md).

## Consulta de existencias y stock mínimo

- **Objetivo:** conocer cantidades disponibles y detectar productos con existencia igual o menor que su mínimo.
- **Entradas:** la lista de productos que está en memoria.
- **Funcionamiento y procesamiento:** el submenú permite consultar todos los productos o solo los que cumplen `existencia <= stock_minimo`. Mostrar código, nombre, cantidad, mínimo y estado; incluir inactivos porque forman parte del inventario físico.
- **Salidas:** las cantidades o un aviso si no hay productos o ninguno está en el mínimo.
- **Reglas y validaciones:** no modificar cantidades durante consultas; incluir cantidades cero y productos cuya cantidad sea igual al mínimo.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Entradas de inventario

- **Objetivo:** aumentar existencias y dejar un registro de la operación.
- **Entradas:** código, cantidad entera positiva, descripción obligatoria y confirmación S/N.
- **Funcionamiento y procesamiento:** buscar el producto, validar datos, mostrar la cantidad resultante y confirmar. Al confirmar, aumentar existencia y agregar movimiento con fecha real, código, tipo `Entrada`, cantidad y descripción. N cancela sin cambios.
- **Salidas:** confirmación con cantidad resultante o avisos de error/cancelación.
- **Reglas:** se permite recibir existencias de un producto inactivo sin reactivarlo; si está inactivo, sigue sin poder venderse. No registrar cantidades cero, negativas ni fracciones.
- **Validaciones y errores:** catálogo vacío, código vacío o inexistente, cantidad inválida, descripción vacía y confirmación distinta de S/N. Una interrupción antes de confirmar no altera el stock ni el historial.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Historial e integración de movimientos

- **Objetivo:** ver las entradas y salidas registradas mientras el programa está abierto.
- **Entradas:** lista `movimientos` creada una sola vez al iniciar el programa.
- **Procesamiento:** cada registro de producto confirmado agrega una `Entrada inicial` con su cantidad (incluido cero). Una edición de cantidad agrega `Ajuste de entrada` o `Ajuste de salida`, con la diferencia positiva, sin movimiento si la cantidad no cambia. Cada línea de venta confirmada agrega una `Salida por venta` con descripción que incluye el número de venta y la misma fecha de la venta. Las entradas manuales usan `Entrada`.
- **Salidas:** historial en orden de registro o aviso de que no hay movimientos.
- **Reglas:** conservar fecha/hora real de America/Guatemala, código, tipo, cantidad y descripción en todos los movimientos. No crear movimientos por consulta, cancelación, edición de otros campos ni venta rechazada. Los precios y totales de venta permanecen independientes del historial de inventario.
- **Validaciones y errores:** lista vacía; si un código se repite en una venta, se suma su cantidad y se registra una sola salida de ese producto. Obtener la fecha antes de cambiar los datos para no descontar si falla ese requisito.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Navegación

La opción 3 del principal abre un submenú: existencias, registrar entrada, stock mínimo, historial y volver (5). Cada operación vuelve al submenú y una opción incorrecta se rechaza sin salir. Las listas solo duran mientras el programa está abierto y se pierden al cerrar.
