# Manual técnico

## Descripción

El programa está hecho en Python y se usa desde la consola. Usa funciones, listas, diccionarios, ciclos, condiciones y `try/except`. Los datos quedan en memoria y se pierden al cerrar.

## Ejecución

Se necesita Python 3.9 o una versión más nueva. El programa se inicia desde la carpeta del proyecto con el comando:

```bash
python3 src/main.py
```

En Windows se puede usar `python` o `py`. Las fechas usan `datetime` y `zoneinfo` para obtener la hora de Guatemala. Si aparece `ZoneInfoNotFoundError` porque el equipo no tiene los datos de zonas horarias, se puede instalar `tzdata` con el mismo Python:

```bash
python -m pip install tzdata
```

El programa utiliza la biblioteca estándar de Python. En equipos sin información de zonas horarias se necesita `tzdata`.

## Archivos y funciones

| Archivo | Función dentro del programa |
| --- | --- |
| `main.py` | Crea las listas y muestra el menú principal. |
| `productos.py` | Registra, busca, lista, modifica y desactiva productos. Valida texto, precio y cantidades. |
| `ventas.py` | Selecciona productos, calcula importes, confirma ventas y descuenta stock. |
| `inventario.py` | Consulta existencias, registra entradas y muestra mínimos y movimientos. |
| `reportes.py` | Calcula ingresos, productos más vendidos, valor de inventario y promedios; también muestra listados e historial. |
| `estructuras.py` | Obtiene la fecha y crea los diccionarios de movimientos. |

Los archivos de esta tabla están en `src`. `tests` contiene pruebas, `docs` la documentación y `evidencias` sus resultados.

## Listas y diccionarios

`main` crea tres listas y las pasa a los módulos:

| Lista | Datos de cada diccionario |
| --- | --- |
| `productos` | `codigo`, `nombre`, `categoria`, `precio`, `existencia`, `stock_minimo`, `activo`. |
| `ventas` | `numero`, `fecha`, `detalle`, `subtotal`, `iva`, `total`. |
| `movimientos` | `fecha`, `codigo`, `tipo`, `cantidad`, `descripcion`. |

El detalle de cada venta es otra lista. Cada línea contiene código, nombre, precio unitario, cantidad y subtotal. Los precios son decimales (`float`), las cantidades son enteros (`int`) y el estado activo es verdadero o falso (`bool`). Las fechas son texto con formato `YYYY-MM-DD HH:MM:SS`, en hora de Guatemala.

## Qué hace cada módulo

**Productos:** `buscar_producto` recorre la lista y devuelve el producto o `None`. El código se convierte a mayúsculas. Si un dato está mal, el programa lo vuelve a pedir. Modificar permite conservar un valor con Enter. Desactivar cambia el estado, sin borrar el producto.

**Ventas:** `registrar_venta` va agregando los productos elegidos a una lista temporal. Valida código, estado y stock, contando las unidades ya elegidas. Calcula los importes antes de confirmar. Con `S` agrega la venta, descuenta cantidades y registra las salidas; con `N` no cambia el stock. El número es `len(ventas) + 1`. La venta guarda el nombre y precio que tenía el producto en ese momento, aunque después se cambien.

**Inventario:** una entrada suma unidades después de confirmar. Cambiar la existencia desde productos registra un ajuste por la diferencia. El stock mínimo compara `existencia <= stock_minimo`, incluidos inactivos. Los movimientos indican entrada inicial, entrada, ajuste de entrada, ajuste de salida o salida por venta.

**Reportes:** recorren los datos de la sesión sin cambiarlos. Para obtener el más vendido, se acumulan cantidades en un diccionario por código y se buscan los mayores; se muestran todos los empates. Si el nombre cambió, este reporte conserva el primero que encuentra en las ventas del código.

## Cálculos y validaciones

| Cálculo | Operación |
| --- | --- |
| Subtotal por producto | Precio unitario redondeado a dos decimales por cantidad. |
| Subtotal general | Suma de subtotales, redondeada a dos decimales. |
| IVA | `round(subtotal * 0.12, 2)` |
| Total | `round(subtotal + iva, 2)` |
| Ingresos | Suma de totales de ventas, incluido IVA. |
| Valor del inventario | Suma de precio redondeado por existencia, con cada resultado redondeado; incluye inactivos. |
| Días del período | `(fin - inicio).days + 1` |
| Promedios diarios | Cantidad de ventas o ingresos divididos entre los días del período. |

Se aceptan precios cero, pero no negativos. Las cantidades son enteras no negativas; las ventas y entradas exigen más de cero. No se admiten códigos repetidos ni campos obligatorios vacíos. Las fechas deben existir y la final no puede ser anterior a la inicial.

`isfinite` comprueba que un importe no sea infinito. `try/except` permite rechazar conversiones o cálculos fuera de rango. Una línea de venta rechazada no altera los totales anteriores. Los importes usan `float` y `round`, con los límites de precisión de Python.

## Pruebas y límites

Desde la raíz del proyecto:

```bash
python3 tests/probar_todo.py
```

Hay 62 pruebas: 25 de productos y menú, 13 de ventas, 12 de inventario y 12 de reportes. Los resultados están en [evidencias/entrega](../evidencias/entrega/). Las entradas y salidas del ejemplo de uso están en [evidencias/manuales](../evidencias/manuales/).

El programa no recupera datos al reiniciar. Al presionar Ctrl+C o terminar la entrada, el programa puede cerrarse. Las funciones de productos y ventas aceptan `movimientos=None` para usarlas por separado; el menú siempre pasa la lista compartida.

Los [diagramas](diagramas/) representan los procesos de Python. El [pseudocódigo](pseint/) incluye procesos separados para PSeInt.

## Evidencias de ejecución

Los registros incluyen 62 pruebas aprobadas de Python y 26 casos de PSeInt. Los [resultados](../evidencias/entrega/) están guardados en archivos de texto.
