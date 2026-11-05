# Pruebas para la entrega

## Sistema Python

El registro de `python3 tests/probar_todo.py` contiene **62 pruebas aprobadas**. Los resultados de productos, ventas, inventario y reportes están en la [salida completa](../evidencias/entrega/python-pruebas.txt).

## Procesos en PSeInt

Se revisó la sintaxis de 12 archivos y se ejecutaron los 26 escenarios siguientes con el intérprete oficial 20250314 y el perfil del proyecto. Cada archivo inicia con datos de ejemplo para probar su proceso por separado.

Los 26 casos dieron los resultados esperados. Aun así, Python y PSeInt tienen diferencias en redondeo, límites de los números y zona horaria. Ver [alcance del pseudocódigo](pseint/README.md).

| Caso | Entradas en orden | Resultado esperado | Resultado obtenido y conclusión |
| --- | --- | --- | --- |
| menu | abc → 1 → 2 → 3 → 4 → 5 | Opcion incorrecta; Hasta luego | Coincidió. Aprobado. |
| registro | P03 → Goma → Utiles → 1.5 → 4 → 1 | P03; Cantidad: 4 | Coincidió. Aprobado. |
| registro invalidos | Enter → P01 → P03 → Enter → Goma → Utiles → -1 → 1.5 → abc → 4 → 1 | Campo obligatorio; codigo ya esta registrado; Numero invalido; P03 | Coincidió. Aprobado. |
| consulta | p01 | Cuaderno; Cantidad: 3 | Coincidió. Aprobado. |
| consulta inexistente | X | No existe | Coincidió. Aprobado. |
| modificar | P01 → Nuevo → Enter → 13 → 5 → 1 | Ajuste de entrada; Producto modificado | Coincidió. Aprobado. |
| conservar | P01 → Enter → Enter → Enter → Enter → Enter | No se realizaron cambios | Coincidió. Aprobado. |
| modificar inexistente | X | No existe | Coincidió. Aprobado. |
| desactivar | P01 → x → s | Respuesta invalida; desactivado | Coincidió. Aprobado. |
| no desactivar | P01 → N | cancelada | Coincidió. Aprobado. |
| ya inactivo | P02 | ya esta inactivo | Coincidió. Aprobado. |
| venta | P01 → 2 → Enter → S | Subtotal: 25; IVA: 3; Total: 28; Salida por venta | Coincidió. Aprobado. |
| venta invalidos | X → P02 → P01 → 0 → 4 → 2 → P01 → 2 → 1 → P01 → Enter → S | No existe; inactivo; mayor que cero; Inventario insuficiente; No hay mas existencias; Total: 42 | Coincidió. Aprobado. |
| venta cancelada | P01 → 2 → Enter → N | Venta cancelada | Coincidió. Aprobado. |
| venta vacia | Enter | No se agregaron productos | Coincidió. Aprobado. |
| entrada | P01 → 4 → Reposicion → S | Cantidad disponible: 7 | Coincidió. Aprobado. |
| entrada invalidos | P01 → 0 → -2 → 3 → Enter → Compra → x → N | mayor que cero; Numero invalido; Campo obligatorio; Respuesta invalida; Entrada cancelada | Coincidió. Aprobado. |
| entrada inactivo | P02 → 3 → Compra → S | Estado: Inactivo; Cantidad disponible: 3 | Coincidió. Aprobado. |
| inventario | x → 1 → 2 → 3 | Opcion incorrecta; Cuaderno; Lapiz | Coincidió. Aprobado. |
| reportes | 1 → 2 → 3 → 4 → 5 → 6 → 8 | Ingresos: 32.48; P01 Unidades: 2; P02 Unidades: 2; Valor del inventario: 37.5 | Coincidió. Aprobado. |
| promedio | 2026-11-01 → 2026-11-03 | Ventas del periodo: 2; Dias del periodo: 3; Ingresos del periodo: 32.48 | Coincidió. Aprobado. |
| fecha invalida | 2026-02-29 → 2026-11-01 → 2026-10-31 → 2026-11-03 | Fecha invalida; anterior; Dias del periodo: 3 | Coincidió. Aprobado. |
| promedio cancelado | Enter | Reporte cancelado | Coincidió. Aprobado. |
| sin ventas periodo | 2020-01-01 → 2020-01-01 | Ventas del periodo: 0; Ingresos del periodo: 0 | Coincidió. Aprobado. |
| listado | Sin entrada | Cuaderno; Lapiz; Inactivo | Coincidió. Aprobado. |
| movimientos | Sin entrada | P01; Entrada inicial; Cantidad: 3 | Coincidió. Aprobado. |

Las entradas y salidas completas están en [ejecuciones.txt](../evidencias/entrega/pseint/ejecuciones.txt); el [resumen](../evidencias/entrega/pseint/resultados.txt) incluye las comprobaciones de sintaxis.

## Evidencias

Las entradas, salidas y resultados están en [evidencias/entrega](../evidencias/entrega/). Las capturas de pantalla aún no están incorporadas.

## Errores corregidos

El intérprete detectó nombres reservados utilizados como identificadores, un nombre de proceso que empezaba con números y una llamada de subproceso mal ubicada en una rama. Se corrigieron y se repitieron las comprobaciones antes de guardar los resultados aprobados.
