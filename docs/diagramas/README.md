# Diagramas de flujo

Estos diagramas muestran los pasos del programa Python. Cada diagrama está disponible en PNG para ver o imprimir, en SVG para ampliar y en DOT como fuente editable. Se generaron con Graphviz y se revisaron contra el código; no son capturas ni exportaciones de PSeInt.

El óvalo marca el inicio o el fin. El paralelogramo sirve para pedir o mostrar datos, el rectángulo para las operaciones y el rombo para las decisiones. Las flechas de regreso representan ciclos. Los rectángulos dobles señalan llamadas a subprocesos; las validaciones compartidas se detallan en el diagrama 13 y en el pseudocódigo.

| Proceso | Imagen |
| --- | --- |
| Menú principal | [01_menu.png](01_menu.png) |
| Registro de productos | [02_registrar_producto.png](02_registrar_producto.png) |
| Consulta por código | [03_consultar_producto.png](03_consultar_producto.png) |
| Modificación | [04_modificar_producto.png](04_modificar_producto.png) |
| Desactivación | [05_desactivar_producto.png](05_desactivar_producto.png) |
| Registro de ventas | [06_registrar_venta.png](06_registrar_venta.png) |
| Entrada de inventario | [07_entrada_inventario.png](07_entrada_inventario.png) |
| Stock mínimo | [08_stock_minimo.png](08_stock_minimo.png) |
| Generación de reportes | [09_reportes.png](09_reportes.png) |
| Promedios por período | [10_promedio_periodo.png](10_promedio_periodo.png) |
| Listado y existencias | [11_listar_productos.png](11_listar_productos.png) |
| Historial de movimientos | [12_historial_movimientos.png](12_historial_movimientos.png) |
| Lectura numérica | [13_validar_numero.png](13_validar_numero.png) |

Para ampliar una imagen, se puede abrir el SVG con el mismo nombre. Para editar el diseño se puede utilizar un editor compatible con Graphviz/DOT; no hace falta instalarlo para usar el programa.

Las operaciones de reportes reutilizan los recorridos y filtros mostrados en los otros diagramas.
