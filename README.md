# Sistema de gestión comercial

Proyecto de Algoritmos 1 hecho en Python. Se usa desde la consola para registrar productos, hacer ventas, revisar el inventario y ver reportes.

## Cómo ejecutarlo

Se necesita Python 3.9 o una versión más nueva. Para iniciar el programa, se abre una terminal en la carpeta del proyecto y se ejecuta:

```bash
python src/main.py
```

Según la instalación, también se puede usar `python3` o `py`. Los errores de zona horaria se explican en el [manual técnico](docs/manual-tecnico.md).

## Opciones del menú

1. Productos: registrar, consultar, listar, modificar y desactivar.
2. Ventas: seleccionar productos, calcular el IVA del 12 % y confirmar la venta.
3. Inventario: consultar existencias, registrar entradas y revisar movimientos.
4. Reportes: consultar ventas, ingresos, stock mínimo y promedios.
5. Salir.

Los datos se guardan en listas y diccionarios mientras el programa está abierto. Al cerrarlo se pierden.

## Carpetas

- `src`: código del programa.
- `docs`: análisis, manuales, diagramas y pseudocódigo.
- `tests`: pruebas de los módulos.
- `evidencias`: entradas, salidas y resultados de las pruebas.

## Documentación

- [Manual de usuario](docs/manual-usuario.md)
- [Manual técnico](docs/manual-tecnico.md)
- [Enunciado](docs/enunciado.md)
- [Análisis de procesos](docs/analisis.md)
- [Diagramas de flujo](docs/diagramas/README.md)
- [Pseudocódigo en PSeInt](docs/pseint/README.md)
- [Pruebas de entrega](docs/pruebas-entrega.md)

## Pruebas

Desde la carpeta del proyecto:

```bash
python tests/probar_todo.py
```

Hay 62 pruebas de productos, ventas, inventario y reportes. Los archivos de PSeInt representan procesos separados y usan datos de ejemplo.
