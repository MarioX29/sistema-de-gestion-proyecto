"""Ejecutar todas las suites conservando los códigos de salida."""

from pathlib import Path
import subprocess
import sys


def main():
    carpeta = Path(__file__).resolve().parent
    for archivo in ["probar_inicio.py", "probar_sistema.py", "probar_ventas.py", "probar_inventario.py", "probar_reportes.py"]:
        print("\nEjecutando " + archivo, flush=True)
        resultado = subprocess.run([sys.executable, str(carpeta / archivo)])
        if resultado.returncode != 0:
            sys.exit(resultado.returncode)
    print("\nTodas las suites terminaron correctamente.")


if __name__ == "__main__":
    main()
