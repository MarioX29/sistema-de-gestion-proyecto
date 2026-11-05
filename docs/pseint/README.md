# Pseudocódigo para PSeInt

Los archivos están en [actual](actual/). Cada uno representa un proceso separado.

## Configuración

Los procesos utilizan un perfil flexible, con funciones de cadenas, subprocesos y arreglos y cadenas con índices desde cero. El perfil está en [perfil-proyecto](actual/perfil-proyecto).

Cada archivo de `actual` se abre y ejecuta por separado en PSeInt. El sistema Python se ejecuta de forma independiente.

| Archivo | Proceso representado |
| --- | --- |
| [01_menu.psc](actual/01_menu.psc) | Repetición, validación y destinos de las opciones del menú. |
| [02_registrar_producto.psc](actual/02_registrar_producto.psc) | Código único, campos obligatorios y valores numéricos. |
| [03_consultar_producto.psc](actual/03_consultar_producto.psc) | Búsqueda y producto inexistente. |
| [04_modificar_producto.psc](actual/04_modificar_producto.psc) | Conservar campos con Enter y ajustar existencias. |
| [05_desactivar_producto.psc](actual/05_desactivar_producto.psc) | Estado y confirmación. |
| [06_registrar_venta.psc](actual/06_registrar_venta.psc) | Selección repetida, stock, cantidades, IVA y confirmación. |
| [07_entrada_inventario.psc](actual/07_entrada_inventario.psc) | Cantidad positiva, descripción y confirmación. |
| [08_consultas_inventario.psc](actual/08_consultas_inventario.psc) | Existencias y stock mínimo. |
| [09_reportes.psc](actual/09_reportes.psc) | Consultas y cálculos sobre datos de ejemplo. |
| [10_promedio_periodo.psc](actual/10_promedio_periodo.psc) | Fechas, período inclusivo y promedios. |
| [11_listar_productos.psc](actual/11_listar_productos.psc) | Recorrido del catálogo, incluidos inactivos. |
| [12_historial_movimientos.psc](actual/12_historial_movimientos.psc) | Recorrido de movimientos. |

## Qué se comprobó

Se utilizó el intérprete oficial PSeInt **20250314**, descargado desde su [sitio oficial](https://pseint.sourceforge.net/index.php?page=descargas.php). Los 12 archivos fueron aceptados en la revisión de sintaxis y se ejecutaron 26 escenarios con entradas normales e inválidas. Las entradas, salidas y resultados están en [evidencias/entrega/pseint](../../evidencias/entrega/pseint/).

En consola se puede reproducir una comprobación con el ejecutable de PSeInt instalado en el equipo:

```bash
pseint docs/pseint/actual/06_registrar_venta.psc --nouser --profile=docs/pseint/actual/perfil-proyecto
```

El programa puede devolver código cero incluso si informa un error; por eso también se revisó que la salida no contuviera `ERROR`. La comprobación inicial detectó identificadores reservados y una llamada mal ubicada; se corrigieron antes de ejecutar los escenarios.

## Diferencias con Python

- Cada archivo funciona por separado. No forman otro programa completo con todos los módulos conectados. El menú muestra los destinos de sus llamadas; no ejecuta los demás `.psc`.
- Los arreglos paralelos representan los diccionarios y listas de Python. Cada archivo carga datos de ejemplo para poder comprobar su proceso. Las fechas y ventas de ejemplo son datos de prueba, no eventos reales.
- Los archivos muestran las validaciones y decisiones del proceso. Las altas de ventas y movimientos se presentan como resultados del proceso aislado; las listas compartidas y su conservación entre menús pertenecen al sistema Python. En el archivo de registro se reserva un espacio adicional para el nuevo producto; esto no impone un límite al programa Python.
- El detalle de ventas se representa por posiciones del catálogo; puede mostrarse en distinto orden del que se seleccionó en Python. Los importes de los casos comprobados coinciden.
- `Redon` de PSeInt no garantiza el mismo resultado que `round` de Python en todos los empates decimales. Las conversiones, la precisión y el desbordamiento también difieren: PSeInt no reproduce `try/except OverflowError` ni todos los límites de `isfinite` de Python. Con números muy grandes, el resultado puede ser distinto al de Python.
- La limpieza de texto quita espacios comunes de los extremos. Python también quita otros espacios y tabulaciones con `strip()`.
- PSeInt obtiene la fecha y la hora con sus funciones incorporadas. En las pruebas se observó una diferencia entre la fecha UTC y la hora local. Los reportes separados usan fechas de ejemplo; el sistema Python usa America/Guatemala.

Los [diagramas en imágenes](../diagramas/) muestran los pasos del programa Python y se hicieron por separado; no se presentan como exportaciones de PSeInt. Se incluye un diagrama adicional de validación numérica, cuyos subprocesos están dentro de los `.psc` que leen números.
