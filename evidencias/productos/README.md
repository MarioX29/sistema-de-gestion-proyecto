# Pruebas de productos

Los casos de esta carpeta revisan el registro, la consulta, los cambios y la desactivación de productos.

- `flujo-normal-entradas.txt` y `flujo-normal-salida.txt`: operaciones con datos válidos.
- `entradas-invalidas-entradas.txt` y `entradas-invalidas-salida.txt`: códigos repetidos, campos vacíos, precios y cantidades incorrectas, productos inexistentes y cancelaciones.
- `pruebas-automatizadas.txt`: resultado de las 25 pruebas de productos y menú.

## Ejecución

```bash
python3 src/main.py < evidencias/productos/flujo-normal-entradas.txt
python3 src/main.py < evidencias/productos/entradas-invalidas-entradas.txt
python3 tests/probar_sistema.py
```

Los dos casos de consola terminaron con código 0. Las entradas se guardan por separado de la salida del programa.
