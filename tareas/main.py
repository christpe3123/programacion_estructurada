# Importamos la función desde el otro archivo
from tareas.calculos import obtener_edad

# Pedimos el dato al usuario
anio = int(input("¿En qué año naciste? "))

# Usamos la función y guardamos el resultado
mi_edad = obtener_edad(anio)

print(f"Tu edad es de {mi_edad} años.")