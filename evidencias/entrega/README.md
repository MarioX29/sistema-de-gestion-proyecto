# Resultados de las pruebas

## Python

El registro de ejecución contiene 62 pruebas aprobadas de productos, ventas, inventario y reportes.

- [Resultados de Python](python-pruebas.txt)

## PSeInt

Los resultados incluyen la revisión de sintaxis de 12 procesos y la ejecución de 26 casos de prueba con el intérprete 20250314 y el perfil del proyecto. Cada proceso utiliza datos de ejemplo.

- [Ejecuciones](pseint/ejecuciones.txt)
- [Resumen de resultados](pseint/resultados.txt)
- [Descripción del pseudocódigo](../../docs/pseint/README.md)

## Evidencias

La carpeta [capturas](capturas/) contiene los registros de entrada y salida de productos, validaciones, ventas, inventario y reportes, además de las ejecuciones de pruebas y PSeInt. Las capturas muestran el uso del sistema y el resultado de las pruebas en Windows.

## Capturas de ejecución

| Captura | Contenido |
| --- | --- |
| [Menú principal](capturas/00_menu.png) | Opciones de acceso a los módulos. |
| [Productos](capturas/01_productos.png) | Consulta de P01: precio 12.50, existencia 3 y mínimo 1. |
| [Validaciones](capturas/02_validaciones.png) | Rechazo de código repetido y registro de P02. |
| [Venta](capturas/03_venta.png) | Venta de 2 unidades, subtotal 25.00, IVA 3.00 y total 28.00. |
| [Inventario](capturas/04_inventario.png) | Entrada de 4 unidades, existencia final 5 e historial. |
| [Reportes](capturas/05_reportes.png) | P01 con 2 unidades vendidas y valor del inventario 62.50. |
| [Ingresos](capturas/05_ingresos.png) | Ingresos por ventas de 28.00, incluido IVA. |
| [Pruebas de productos](capturas/06_pruebas_productos.png) | Las 25 pruebas de productos y menú completadas. |
| [Resultado final](capturas/06_pruebas.png) | Finalización correcta del conjunto de pruebas de Python. |
