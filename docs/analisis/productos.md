# Gestión de productos en memoria

Aquí se explica cómo funciona la parte de productos que pide el [enunciado](../enunciado.md). Incluye enlaces a los [diagramas](../diagramas/README.md) y al [pseudocódigo para PSeInt](../pseint/README.md).

## Datos y reglas compartidas

Cada producto se guarda en un diccionario de la lista `productos`:

| Dato | Regla |
| --- | --- |
| `codigo` | Texto obligatorio, sin espacios externos y en mayúsculas. Único, incluso si el producto está inactivo. Se conserva al modificar. |
| `nombre` | Texto obligatorio sin espacios externos. |
| `categoria` | Texto obligatorio sin espacios externos. |
| `precio` | Número decimal desde cero, sin aceptar infinito. Se permite cero porque el enunciado prohíbe precios negativos. |
| `existencia` | Cantidad disponible: entero mayor o igual a cero. |
| `stock_minimo` | Entero mayor o igual a cero; puede superar la existencia actual. |
| `activo` | Verdadero al registrar; falso al desactivar. No se elimina el producto. |

Los campos numéricos aceptan dígitos 0–9, punto para el precio y sin signos, comas ni notación científica. Las cantidades enteras aceptan hasta 4300 dígitos; también se rechazan conversiones fuera del rango admitido por Python. Cada vez que se abre el programa, la lista empieza vacía.

La opción 1 del menú principal abre un submenú: registrar, consultar, listar, modificar, desactivar y volver al menú principal. Cada operación regresa al submenú y la opción 6 permite volver al principal. Una opción incorrecta produce un aviso y repite el submenú.

## Registro de productos

- **Objetivo:** agregar un producto con todos los campos mínimos del enunciado.
- **Funcionamiento:** solicitar cada campo y repetir únicamente los que sean inválidos.
- **Entradas:** código, nombre, categoría, precio, existencia inicial y stock mínimo, en ese orden.
- **Procesamiento:** quitar espacios al inicio y al final del código, pasarlo a mayúsculas y buscarlo; validar campos; agregar el diccionario completo a la lista con estado activo.
- **Salidas:** mensajes de error o confirmación del registro.
- **Reglas de negocio:** no duplicar códigos ni aceptar cantidades o precios negativos. Aceptar precio y cantidades en cero.
- **Validaciones y errores:** campos vacíos, código ya registrado, texto en campos numéricos, decimales en cantidades, valores no finitos y conversiones demasiado grandes. No agregar datos parciales.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Consulta por código

- **Objetivo:** encontrar y mostrar un producto específico.
- **Funcionamiento:** pedir el código, quitar los espacios de sus extremos, pasarlo a mayúsculas y recorrer la lista para buscarlo.
- **Entradas:** código obligatorio.
- **Procesamiento:** comparar códigos y mostrar todos los campos del producto encontrado.
- **Salidas:** datos del producto o un aviso si no existe o no hay productos registrados.
- **Reglas de negocio:** incluir productos activos e inactivos e indicar su estado.
- **Validaciones y errores:** repetir un código vacío; un código inexistente no modifica la lista ni termina el programa.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Listado de productos

- **Objetivo:** consultar el catálogo completo durante la sesión.
- **Funcionamiento:** recorrer la lista y mostrar los datos de cada producto.
- **Entradas:** la lista de productos, sin pedir otros datos.
- **Procesamiento:** mostrar código, nombre, categoría, precio, existencia, stock mínimo y estado.
- **Salidas:** fichas de todos los productos o aviso de catálogo vacío.
- **Reglas de negocio:** conservar el orden de registro e incluir los inactivos sin ocultar su estado.
- **Validaciones y errores:** manejar una lista vacía sin fallar ni modificar datos.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Modificación de productos

- **Objetivo:** actualizar la información de un producto existente.
- **Funcionamiento:** buscar por código y solicitar nombre, categoría, precio, existencia y stock mínimo. Enter conserva el valor actual de un campo.
- **Entradas:** código obligatorio y nuevos datos para los cinco campos que se pueden cambiar; Enter deja el dato anterior.
- **Procesamiento:** mostrar la ficha actual, revisar los nuevos valores y guardarlos juntos al terminar de pedir los datos.
- **Salidas:** confirmación de modificación, aviso de que no hubo cambios o mensaje de producto inexistente/catálogo vacío.
- **Reglas de negocio:** conservar código y estado; no registrar otro producto ni reactivar uno inactivo. Se permite corregir información de un producto inactivo. Si cambia la existencia, se registra un ajuste de entrada o salida por la diferencia.
- **Validaciones y errores:** las mismas reglas del registro para los datos que se escriban; Enter significa conservar, no borrar. Rechazar negativos y tipos incorrectos. No aplicar cambios parciales si se interrumpe la lectura antes de completar todos los campos.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).

## Desactivación de productos

- **Objetivo:** marcar que un producto ya no está disponible para la venta sin eliminar su información.
- **Funcionamiento:** buscar el código, mostrar la ficha y pedir confirmación S/N.
- **Entradas:** código obligatorio y confirmación.
- **Procesamiento:** si el producto existe y está activo, cambiar únicamente `activo` a falso al confirmar S. N cancela y una confirmación inválida se vuelve a pedir.
- **Salidas:** confirmación, aviso de cancelación, producto ya inactivo, producto inexistente o catálogo vacío.
- **Reglas de negocio:** conservar los datos y el lugar del producto en la lista; no permitir reutilizar su código. El módulo de ventas rechaza los productos inactivos.
- **Validaciones y errores:** validar el código y la confirmación; repetir la desactivación no debe eliminar datos ni producir errores.
- **Diagrama:** [consultar imágenes del proceso](../diagramas/README.md).
