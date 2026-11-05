# Pruebas de productos

Los resultados generales están en [pruebas de entrega](pruebas-entrega.md).

## Ejecución y resultado general

El registro de `python3 tests/probar_sistema.py` contiene 25 pruebas aprobadas. La salida está en [pruebas-automatizadas.txt](../evidencias/productos/pruebas-automatizadas.txt).

## Casos, datos y resultados

En esta tabla, la ficha base es `P1`, `Cuaderno`, `Útiles`, precio `12.50`, existencia `3`, stock mínimo `1`, activo. Cada prueba usa su propia lista; no depende de datos de pruebas anteriores.

| Caso | Datos utilizados | Resultado esperado | Resultado obtenido | Conclusión |
| --- | --- | --- | --- | --- |
| Salida | `5`, seguido de `1` | Salir sin procesar la segunda entrada. | Una despedida, sin solicitar código. | Aprobada. |
| Opciones incorrectas | `0`, `6`, `-1`, `abc`, vacío, `1.5`, `15`, `5` en el principal | Siete avisos y salida con 5. | Siete avisos, ocho menús y código 0. | Aprobada. |
| Registro normal | ` p01 `, ` Cuaderno `, ` Útiles `, `12.50`, `3`, `1` | Guardar siete campos normalizados. | Diccionario completo, código P01 y estado activo. | Aprobada. |
| Campos obligatorios | Vacío y espacios en código, nombre y categoría; existencia y mínimo cero | Repetir los textos vacíos y aceptar cero. | Dos avisos por campo obligatorio y un producto registrado. | Aprobada. |
| Duplicado | Registrar P1; intentar ` p1 ` y `P1`, luego P2 | Rechazar duplicados y conservar el primero. | Dos rechazos; dos productos con códigos diferentes. | Aprobada. |
| Precio inválido | Vacío, espacios, `abc`, `-1`, `1,5`, `1.2.3`, `.`, `NaN`, `inf`, `1e3`, 400 nueves; finalmente `2.75` | Rechazar 11 entradas y guardar 2.75. | Once avisos y un producto con precio 2.75. | Aprobada. |
| Existencia inválida | Vacío, espacios, `abc`, `-1`, `1.5`, `1,5`, `NaN`, `inf`, `1e2`, `²`, 5000 nueves; luego cero | Rechazar 11 entradas y aceptar cero. | Once avisos y existencia entera cero. | Aprobada. |
| Formatos numéricos válidos | Precios `.5` y `2.`, existencia `01` | Guardar 0.5, 2.0 y entero 1. | Valores esperados en dos productos. | Aprobada. |
| Reinicio | Registrar P1 en dos procesos separados | La segunda sesión no conserva el primer registro. | Ambos procesos aceptaron P1 sin duplicado. | Aprobada. |
| Precio cero y mínimo superior | Precio 0, existencia 0, mínimo 5 | Aceptar valores no negativos y mínimo mayor a existencia. | Se guardaron 0, 0 y 5. | Aprobada. |
| Mínimo inválido | Vacío, `-1`, `1.5`, `abc`, `NaN`, `1e3`, 5000 nueves; luego 2 | Rechazar siete entradas y guardar 2. | Siete avisos y mínimo entero 2. | Aprobada. |
| Consulta | Ficha base; código vacío y luego ` p1 ` | Repetir código vacío y mostrar todos los campos. | Ficha completa, sin modificar la lista. | Aprobada. |
| Inexistente | `NO-EXISTE` en consulta, modificación y desactivación | Avisar sin cambiar los datos. | Tres operaciones sin cambios ni errores. | Aprobada. |
| Catálogo vacío | Consultar, listar, modificar y desactivar sobre `[]` | Avisar sin solicitar datos ni fallar. | Cuatro avisos y lista vacía conservada. | Aprobada. |
| Listado | P1 activo y P2 inactivo | Mostrar ambos en orden, con estado y campos. | Dos fichas ordenadas; catálogo sin cambios. | Aprobada. |
| Modificación | P1 a Libreta, Oficina, precio 0, cantidad 0, mínimo 2; P2 existente | Actualizar cinco campos de P1 y conservar P2. | Valores esperados y dos productos. | Aprobada. |
| Conservar campos | P1 inactivo; Enter en los cinco campos, luego cambiar solo nombre | No alterar al conservar; editar nombre sin reactivar. | Aviso sin cambios y posterior edición manteniendo estado inactivo. | Aprobada. |
| Edición inválida | Precio `-1`, `NaN`, `abc`, luego 1.25; cantidad `-2`, `2.5`, luego 5; mínimo `-1`, `xyz`, luego 0 | Repetir cada campo incorrecto y aplicar solo valores válidos. | Tres, dos y dos avisos; valores finales 1.25, 5 y 0. | Aprobada. |
| Lectura interrumpida | Simular fin de entrada antes del mínimo en registro y edición | No guardar un registro parcial ni editar parcialmente. | La lista original quedó intacta en ambos casos. | Aprobada; no implica captura del fin de entrada por el menú. |
| Desactivación | P1, respuestas vacío, `sí`, ` s `; después repetir | Dos avisos, desactivar sin borrar y avisar si ya está inactivo. | Solo cambió el estado; repetición sin cambios. | Aprobada. |
| Cancelación | P1 y respuesta ` n ` | No desactivar. | Cancelación y ficha original intacta. | Aprobada. |
| Código inactivo | P1 inactivo; intentar ` p1 `, luego registrar P2 y consultar P1 | No reutilizar el código y permitir consultar el inactivo. | Duplicado rechazado, P2 agregado y P1 mostrado inactivo. | Aprobada. |
| Submenú completo | Cuatro opciones incorrectas, catálogo vacío, registrar, consultar, listar, modificar, cancelar y confirmar desactivación, salir y reingresar al módulo | Ejecutar las cinco operaciones y conservar datos durante la sesión. | Mensajes esperados, estado inactivo conservado al reingresar y salida 0. | Aprobada. |

## Evidencias adicionales

Se ejecutaron dos escenarios completos como procesos reales del programa: flujo normal y entradas inválidas. Ambos terminaron con código 0. Sus entradas, salidas y comandos para repetirlos están en [evidencias/productos](../evidencias/productos/README.md).

Las pruebas que inspeccionan diccionarios usan entradas controladas con `unittest.mock`; las pruebas de consola ejecutan `src/main.py` en procesos separados.

El registro de resultados contiene 25 pruebas aprobadas.

## Alcance

El rechazo de enteros de 5000 dígitos se comprobó con la configuración predeterminada de Python 3.12.14. Las pruebas de los otros módulos están en sus respectivos documentos.
