from datetime import datetime

def obtener_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    resultado = anio_actual - anio_nacimiento
    return resultado