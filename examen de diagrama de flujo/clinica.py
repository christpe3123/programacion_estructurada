class Clinica:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.doctores = []
        self.pacientes = []
        self.reseccionistas = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_reseccionista(self, reseccionista):
        self.reseccionistas.append(reseccionista)
class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Reseccionista:
    def __init__(self, nombre):
        self.nombre = nombre
        