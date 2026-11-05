from datetime import datetime
from zoneinfo import ZoneInfo


def fecha_actual():
    zona = ZoneInfo("America/Guatemala")
    fecha = datetime.now(zona)
    return fecha.strftime("%Y-%m-%d %H:%M:%S")


def crear_movimiento(codigo, tipo, cantidad, descripcion, fecha=None):
    if fecha is None:
        fecha = fecha_actual()
    movimiento = {
        "fecha": fecha,
        "codigo": codigo,
        "tipo": tipo,
        "cantidad": cantidad,
        "descripcion": descripcion
    }
    return movimiento

