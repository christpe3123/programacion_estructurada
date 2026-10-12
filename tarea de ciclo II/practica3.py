#caso2 Registro académico con recuperación - 7 puntos
#El docente desea distinguir a quienes aprobaron directamente de quienes necesitan recuperación, y
#obtener un resumen del aula.


alumnos = [
    {"nombre": "Ana", "notal": 18, "nota2": 16},
    {"nombre": "Luis", "notal": 9, "nota2": 14},
    {"nombre": "Marta", "notal": 15, "nota2": 17},
    {"nombre": "Jose", "notal": 10, "nota2": 11},
    {"nombre": "Pedro", "notal": 13, "nota2": 13},
    {"nombre": "Rosa", "notal": 12, "nota2": 12}
]

for alumno in alumnos:
    print("primera nota")
    if alumno["notal"] >= 13:
        print(f"{alumno["nombre"]} aprobó {alumno["notal"]}")
    else:
        print(f"{alumno["nombre"]} no aprobó  {alumno["notal"]}")
    print("segunda nota")
    if alumno["nota2"] >= 13:
        print(f"{alumno["nombre"]} aprobó {alumno["nota2"]}")
    else:
        print(f"{alumno["nombre"]} no aprobó  {alumno["nota2"]}")
    print("recuperacion de nota 1")
    if alumno["notal"] > 13 and 10:
        print(f"{alumno["nombre"]} aprobó {alumno["notal"]}")
    print("recuperacion de nota 2")
    if alumno["nota2"] > 13 and 10:
            print(f"{alumno["nombre"]} aprobó {alumno["nota2"]}")
    if alumno["notal"] and alumno["nota2"] >= 13:
            print(f"{alumno["nombre"]} promedio de nota {alumno["notal"]}")
    if alumno["nota2"] > alumno["notal"]:
            print(f"{alumno['nombre']}  {alumno["nota2"]} > {alumno["notal"]}")
            
