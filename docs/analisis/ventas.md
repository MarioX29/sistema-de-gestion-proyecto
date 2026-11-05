# Registro de ventas en memoria

Aquí se explica cómo se registra y confirma una venta. Ver [diagramas](../diagramas/README.md) y [pseudocódigo](../pseint/README.md).

## Objetivo y funcionamiento

Vender uno o varios productos activos, calcular lo que hay que pagar y descontar las cantidades solo al confirmar. La opción 2 del principal inicia una venta y luego regresa al menú.

## Entradas

Códigos de productos, cantidades enteras positivas y confirmación S/N. Enter en el código finaliza la selección; sin productos cancela la venta. Se utiliza el catálogo de la sesión, incluidos precios y existencias actuales.

## Procesamiento

1. Comprobar que haya algún producto activo con existencias positivas.
2. Quitar los espacios de los extremos del código, pasarlo a mayúsculas y buscarlo. Rechazar inexistentes, inactivos y productos sin existencia.
3. Mostrar el nombre, el precio unitario con dos decimales y las unidades que quedan disponibles para agregar. Después pedir la cantidad; rechazar cero, negativos, tipos incorrectos o cantidades superiores a lo disponible. Si se repite un código, acumular su cantidad y contar las unidades ya elegidas para no vender más de las que hay.
4. Calcular el subtotal de cada producto, el subtotal general, IVA del 12 % y total. Guardar precio unitario y nombre como copia de los datos de la venta, para que futuras ediciones del catálogo no alteren su historial.
5. Mostrar el resumen y pedir confirmación. N cancela; una respuesta inválida se repite. No modificar catálogo ni historial mientras se prepara o cancela la venta.
6. Al confirmar, descontar existencias y agregar la venta a la lista en memoria, con número consecutivo desde 1 y fecha/hora del equipo en la zona America/Guatemala.

## Salidas

Detalle con cantidades y subtotales, subtotal general, IVA, total y número de venta confirmada; o avisos de error/cancelación. Después vuelve al menú principal.

## Reglas y validaciones

- Las cantidades deben ser enteras y mayores que cero. Se cuentan también las unidades que ya se agregaron a la venta.
- Reutilizar las validaciones de enteros y la búsqueda del módulo de productos.
- Los productos de precio cero son válidos según el enunciado.
- Redondear el precio unitario usado en ventas y los importes a dos decimales mediante `round` de Python; sumar los subtotales redondeados y calcular IVA sobre ese subtotal. No redondear solo al mostrar. Se usa el redondeo de `round` y la precisión de `float`, sin instalar otras bibliotecas.
- Rechazar operaciones cuyo importe no sea finito o cuya conversión exceda el rango numérico; no dejar cantidades reservadas por ese intento.
- Cancelar una venta no usa un número. Tampoco se guardan ventas sin productos.
- Una lectura interrumpida antes de confirmar no debe registrar ventas ni descontar stock.
- Cada línea de una venta confirmada agrega una salida al historial de movimientos, con la fecha y el número de venta.

## Errores y alternativas

Si no hay productos o ninguno se puede vender, mostrar el aviso y volver al menú. Código inválido: informar y pedir otro. Cantidad cero o superior al disponible: volver a solicitar la cantidad. Puede ingresarse una cantidad válida y luego cancelar la venta al confirmar. El sistema no permite editar ni eliminar ventas confirmadas.

**Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).
