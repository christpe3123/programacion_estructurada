#clinica
#doctor
#paciente
#reseccionista
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

#Doctor se prepara para atender a los pacientes

print("Doctor se prepara para atender a los pacientes.")

#el primer paciente llega al consultorio del doctor para un chequeo

print("Primer paciente llega al consultorio del doctor para un chequeo.")

#doctor le pregunta sobre sus malestares y le da un diagnóstico

malestares = input("Doctor: ¿Cuáles son sus malestares? ")

diagnostico = "Gripe común"

print(f"Doctor diagnostica al paciente con {diagnostico}.")

if diagnostico == "Gripe común":
    print("Doctor recomienda reposo y tomar líquidos.")
else:
    print("Doctor recomienda realizar más pruebas para un diagnóstico preciso.")

#registra la atencion en el historial del paciente

print("Doctor registra la atención en el historial del paciente.")

#genera documento de receta médica para el paciente

print("Doctor genera documento de receta médica para el paciente.")

receta_medica = f"Receta médica para {malestares}: Reposo y tomar líquidos."

print(receta_medica)

#el doctor le da la receta al paciente y le indica que se retire de la clínica

print("Doctor le da la receta al paciente y le indica que se retire de la clínica.")

#el segundo paciente llega al consultorio del doctor para una consulta

print("Segundo paciente llega al consultorio del doctor para una consulta.")

#el doctor ve el historial del paciente y le pregunta sobre sus síntomas

sintomas = input("Doctor: ¿Cuáles son sus síntomas? ")

print(f"Doctor revisa el historial del paciente y le pregunta sobre sus síntomas: {sintomas}.")

#el doctor le da un diagnóstico al paciente

diagnostico2 = "tumor"

print(f"Doctor diagnostica al paciente con {diagnostico2}.")

#necesita una operacion para extirpar el tumor

print("Doctor indica que el paciente necesita una operación para extirpar el tumor.")

#puede operarse ahorita o programar una cita para la operación
if diagnostico2 == "tumor":
    print("Doctor indica que el paciente puede operarse ahorita o programar una cita para la operación.")
else:
    print("Doctor indica que el paciente no necesita una operación y le da recomendaciones para su tratamiento.")

#empieza a operar al paciente o programa una cita para la operación
opcion_operacion = input("¿Desea operarse ahorita? (si/no): ")
if opcion_operacion.lower() == "si":
    print("Doctor empieza a operar al paciente.")
else:
    print("Doctor programa una cita para la operación.")

#operacion exitosa y el paciente se recupera
print("Operación exitosa y el paciente se recupera.")
operacion_exitosa = True
if operacion_exitosa:
    print("Paciente se recupera exitosamente después de la operación.")
#doctor registra la operación en el historial del paciente
print("Doctor registra la operación en el historial del paciente.")
historial_operacion = f"Operación para extirpar tumor realizada con éxito."
print(historial_operacion)