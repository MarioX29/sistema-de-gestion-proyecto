# Análisis de procesos

El sistema permite administrar productos, registrar ventas, controlar inventario y consultar reportes. Todos los módulos usan las mismas listas de productos, ventas y movimientos mientras el programa está abierto. Los datos se pierden al cerrar.

## Menú principal

- **Nombre:** selección de módulo.
- **Objetivo:** elegir qué hacer y cerrar el programa con la opción de salir.
- **Entradas:** la opción que se escribe en el menú.
- **Funcionamiento:** mostrar las cinco opciones, quitar espacios externos de la respuesta y ejecutar la operación correspondiente.
- **Procesamiento:** 1 abre productos; 2 registra una venta; 3 abre inventario; 4 abre reportes; 5 termina el programa.
- **Salidas:** menú, mensajes de opción incorrecta, resultados del módulo o despedida.
- **Reglas:** usar las mismas listas al pasar de un módulo a otro. Cada submenú tiene una opción para volver al principal.
- **Validaciones:** una opción distinta de 1, 2, 3, 4 o 5 muestra un aviso y repite el menú.
- **Diagrama:** [menú principal](diagramas/01_menu.png).

## Procesos de cada módulo

| Módulo | Análisis |
| --- | --- |
| Productos | [Registro, consulta, listado, modificación y desactivación](analisis/productos.md). |
| Ventas | [Selección de productos, validación de stock, IVA y confirmación](analisis/ventas.md). |
| Inventario | [Existencias, entradas, stock mínimo y movimientos](analisis/inventario.md). |
| Reportes | [Listados, ingresos, unidades vendidas, valor del inventario y promedios](analisis/reportes.md). |

Cada documento describe objetivos, entradas, procesamiento, salidas, reglas y validaciones.

## Diagramas y pseudocódigo

Los [diagramas de flujo](diagramas/README.md) muestran decisiones, ciclos y rutas de error. El [pseudocódigo para PSeInt](pseint/README.md) muestra cada proceso por separado. Ya se comprobó su sintaxis y se ejecutaron casos de prueba. En su documentación se explican las diferencias con Python y los límites de los números.

En esta entrega los datos quedan en memoria.
