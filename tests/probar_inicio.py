"""Pruebas de inicio con y sin datos de zona horaria."""

import io
from contextlib import redirect_stdout
from pathlib import Path
import sys
from unittest.mock import patch
from zoneinfo import ZoneInfoNotFoundError


raiz = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(raiz / "src"))
import main as programa


def probar_inicio_con_zona_horaria():
    salida = io.StringIO()
    with patch("builtins.input", side_effect=["5"]), redirect_stdout(salida):
        programa.main()
    assert "Sistema de gestión comercial" in salida.getvalue()
    assert "Hasta luego." in salida.getvalue()
    assert "pip install tzdata" not in salida.getvalue()


def probar_inicio_sin_zona_horaria():
    salida = io.StringIO()
    with patch("main.fecha_actual", side_effect=ZoneInfoNotFoundError("America/Guatemala")):
        with patch("builtins.input", side_effect=AssertionError("No debe abrir el menú")), redirect_stdout(salida):
            programa.main()
    texto = salida.getvalue()
    assert "America/Guatemala" in texto
    assert "python -m pip install tzdata" in texto
    assert "py -m pip install tzdata" in texto
    assert "Sistema de gestión comercial" not in texto
    assert "Traceback" not in texto


def main():
    pruebas = [probar_inicio_con_zona_horaria, probar_inicio_sin_zona_horaria]
    for prueba in pruebas:
        prueba()
        print("PASS:", prueba.__name__)
    print(str(len(pruebas)) + " pruebas de inicio completadas correctamente.")


if __name__ == "__main__":
    main()
