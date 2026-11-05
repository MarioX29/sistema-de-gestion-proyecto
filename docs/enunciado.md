# Instrucciones Generales

Instrucciones generales:

En grupos no mayores a 3 integrantes.

Objetivo

Desarrollar un sistema de gestión comercial para una pequeña empresa, utilizando Python. El sistema permitirá administrar productos, controlar inventarios, registrar ventas y generar reportes estadísticos.

Además del desarrollo del programa, se deberá realizar el análisis de cada proceso, elaborar diagramas de flujo, documentar el funcionamiento del sistema y utilizar GitHub para administrar y publicar el código fuente.

Requerimientos funcionales:

El sistema deberá contar con un menú principal que permita acceder a todos los módulos.

El menú deberá:

- Mostrar las opciones disponibles.
- Validar la opción seleccionada.
- Permitir regresar al menú principal después de cada operación.
- Evitar que el programa finalice por una opción inválida.
- Incluir una opción para salir del sistema de forma controlada.

**Modulo 1 - Gestión de Productos**

El sistema deberá permitir:

- Registrar productos.
- Consultar productos por código.
- Mostrar el listado de productos.
- Modificar la información de un producto.
- Desactivar productos cuando ya no se encuentren disponibles para la venta.

Cada producto deberá contar, como mínimo, con código, nombre, categoría, precio de venta, cantidad disponible y stock mínimo.

No se permitirá registrar códigos duplicados ni precios o cantidades negativos.

**Modulo 2 - Registro de Ventas**

Para cada venta deberá:

- Solicitar los productos y las cantidades que se desean vender.
- Verificar que los productos existan.
- Validar que las cantidades sean positivas.
- Verificar que exista suficiente inventario.
- Calcular el subtotal de cada producto.
- Calcular el subtotal general, el IVA del 12 % y el total de la venta.
- Generar un número de venta.
- Actualizar las existencias.

**Modulo 3 - Control de inventarios**

- Consultar las existencias de los productos.
- Registrar entradas de inventario.
- Actualizar las cantidades disponibles.
- Identificar productos que hayan alcanzado o estén por debajo del stock mínimo.
- Consultar el historial de movimientos de inventario.

Cada movimiento deberá registrar, como mínimo, fecha, código del producto, tipo de movimiento, cantidad y descripción.

**Modulo 4 - Reportes y Estadísticas**

El sistema deberá generar, como mínimo, los siguientes reportes:

- Listado general de productos.
- Productos con existencias iguales o inferiores al stock mínimo.
- Historial de ventas.
- Total de ingresos por ventas.
- Producto con mayor cantidad de unidades vendidas.
- Valor total del inventario disponible.
- Promedio de ventas por período, según los datos registrados.

Los resultados deberán calcularse a partir de la información almacenada y no mediante valores escritos directamente en el código.

**Análisis**

Antes de implementar cada módulo, el equipo deberá analizar los procesos que lo componen.

Para cada proceso funcional principal se deberá documentar:

- Nombre del proceso.
- Objetivo.
- Descripción del funcionamiento.
- Datos de entrada.
- Procesamiento realizado.
- Datos de salida.
- Reglas de negocio.
- Validaciones y posibles errores.
- Diagrama de flujo correspondiente.

Como mínimo, se deberán analizar y representar los procesos de registro de productos, consulta y modificación de productos, registro de ventas, actualización de inventario y generación de reportes.

Los diagramas deberán utilizar símbolos normalizados y mostrar las decisiones, ciclos, validaciones y rutas alternativas que correspondan.

Se recomienda elaborar los diagramas mediante diagrams.net y guardar las imágenes dentro del repositorio de GitHub.

**Pruebas del Sistema**

El equipo deberá diseñar y ejecutar casos de prueba que permitan comprobar el funcionamiento de los diferentes módulos.

Se deberán incluir pruebas normales y pruebas de situaciones excepcionales, tales como:

- Registrar un producto con datos válidos.
- Intentar registrar un código duplicado.
- Ingresar cantidades negativas o datos de tipo incorrecto.
- Intentar vender más unidades de las disponibles.
- Consultar un producto inexistente.
- Verificar los resultados de los cálculos.

Para cada prueba se deberá documentar el caso, los datos utilizados, el resultado esperado, el resultado obtenido y la conclusión.

Se deberán incluir capturas de pantalla que evidencien la ejecución de las pruebas.

**Uso obligatorio de GitHub**

Cada equipo deberá crear un repositorio en GitHub para administrar el código fuente y la documentación del proyecto.

El repositorio deberá:

- Tener un nombre relacionado con el sistema desarrollado.
- Incluir un archivo README.md.
- Mantener una estructura ordenada de carpetas y archivos.
- Contener el código fuente, diagramas, análisis, manuales y evidencias.
- Registrar al menos ocho commits significativos durante el desarrollo.
- Incluir una rama para desarrollar una funcionalidad y un pull request para integrar los cambios.
- Utilizar Issues para registrar al menos un problema detectado y una mejora o tarea pendiente.
- Contar con una versión final identificable mediante una etiqueta o release.

Los mensajes de los commits deberán describir los cambios realizados. No se considerarán suficientes mensajes genéricos como “cambio”, “actualización” o “versión final” si no permiten identificar el trabajo efectuado.

Todos los integrantes deberán participar en el desarrollo y mantener evidencia verificable de sus aportes.

No se deberán publicar contraseñas, credenciales, datos personales ni información sensible.

**El repositorio deberá organizarse de forma similar a la siguiente:**

sistema-gestion-comercial/

- README.md
- .gitignore
- src/
  - main.py
  - productos.py
  - ventas.py
  - inventario.py
  - reportes.py
  - estructuras.py

* docs/
  - analisis/
  - diagramas/
  - manual-tecnico.md
  - manual-usuario.md
* evidencias/

**Manual Técnico**

**Manual de usuario**

necesidad de conocer Python.

Deberá incluir:

1. Presentación y propósito del sistema.
2. Requisitos para utilizarlo.
3. Instrucciones para iniciar y cerrar el programa.
4. Explicación del menú principal.
5. Procedimiento para registrar, consultar y modificar productos.
6. Procedimiento para registrar ventas.
7. Procedimiento para consultar y actualizar inventario.
8. Instrucciones para generar y consultar reportes.
9. Explicación de los mensajes de error más frecuentes.
10. Ejemplos de uso con capturas de pantalla.

Las instrucciones deberán presentarse en orden y permitir que una persona pueda realizar las operaciones sin solicitar ayuda a los desarrolladores.

Al finalizar el proyecto, cada equipo deberá presentar:

1. Enlace público al repositorio de GitHub.
2. Código fuente completo y funcional.
3. Archivos de prueba necesarios para ejecutar el sistema.
4. Documento de análisis de los procesos.
5. Diagramas de flujo de los procesos requeridos.
6. Manual técnico.
7. Manual de usuario.
8. Evidencias de las pruebas realizadas.
9. Historial de commits, rama y pull request.
10. Versión final identificable mediante una etiqueta o release.
11. Presentación y demostración funcional del sistema.

El repositorio deberá permitir que el docente descargue el proyecto, siga las instrucciones y ejecute el programa sin depender de archivos almacenados únicamente en la computadora de alguno de los integrantes.
