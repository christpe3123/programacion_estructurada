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

#el usuario entra a la clinica

clinica = Clinica("Clinica San Jose", "Calle 123")

#se dirige a la recepcionista

recepcionista = Reseccionista("Maria")

clinica.agregar_reseccionista(recepcionista)

#la recepcionista le pregunta su nombre y edad

nombre_paciente = input("Ingrese su nombre: ")

edad_paciente = input("Ingrese su edad: ")

dni_paciente = input("Ingrese su DNI: ")

#la recepcionista registra al paciente

paciente = Paciente(nombre_paciente, edad_paciente)

clinica.agregar_paciente(paciente)

print(f"Paciente {paciente.nombre} registrado con éxito en la clínica {clinica.nombre}.")

#el paciente se dirige al doctor para un chequeo

doctor = Doctor("Dr. Smith", "General")

clinica.agregar_doctor(doctor)

print(f"Paciente {paciente.nombre} se dirige al doctor {doctor.nombre} para un chequeo.")

#doctor le pregunta sobre sus malestares y le da un diagnóstico

malestares = input("Doctor: ¿Cuáles son sus malestares? ")

diagnostico = "Gripe común"

print(f"Doctor {doctor.nombre} diagnostica al paciente {paciente.nombre} con {diagnostico}.")

if diagnostico == "Gripe común":
    print("Doctor recomienda reposo y tomar líquidos.")
else:
    print("Doctor recomienda realizar más pruebas para un diagnóstico preciso.")


#el paciente se retira de la clínica

print(f"Paciente {paciente.nombre} se retira de la clínica {clinica.nombre}.")

#tiene que hacer una cita para una consulta de seguimiento

cita_seguimiento = input("¿Desea agendar una cita de seguimiento? (sí/no) ")

if cita_seguimiento.lower() == "sí":
    print("Cita de seguimiento agendada con éxito.")
else:    print("No se ha agendado una cita de seguimiento.")

#el paciente regresa a la reseccionista para pagar su consulta y guardar su información y programarlo para la siguiente consulta

print(f"Paciente {paciente.nombre} regresa a la recepcionista para pagar su consulta y guardar su información.")

#la recepcionista le pregunta su nombre para buscar su información

nombre_paciente_pago = input("Ingrese su nombre para buscar su información: ")

#la recepcionista busca al paciente en el sistema

print("Recepcionista busca al paciente en el sistema.")

print(f"Paciente {nombre_paciente_pago} encontrado en el sistema.")

#la recepcionista le informa el monto a pagar

monto_a_pagar = 100  # Ejemplo de monto a pagar

print(f"Recepcionista informa al paciente {nombre_paciente_pago} que el monto a pagar es ${monto_a_pagar}.")

#el paciente paga y se retira de la clínica

print(f"Paciente {nombre_paciente_pago} paga el monto de ${monto_a_pagar} y se retira de la clínica {clinica.nombre}.")

# Y la reseccionista le dice el dia y la hora de su siguiente consulta

print(f"Recepcionista informa al paciente {nombre_paciente_pago} que su siguiente consulta está programada para el día viernes a las 10:00 am.")

