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


# resepcionista se prepara para registrar los datos de los pacientes   

print("Recepcionista se prepara para registrar los datos de los pacientes.")

# el primer paciente llega a la clínica y le pide sus datos para una consulta

print("Primer paciente llega a la clínica y le pide sus datos para una consulta.")

# la recepcionista le pregunta su nombre y edad

nombre_paciente1 = input("Ingrese su nombre: ")

edad_paciente1 = input("Ingrese su edad: ")

# la recepcionista registra al paciente

paciente1 = Paciente(nombre_paciente1, edad_paciente1)

clinica = Clinica("Clinica San Jose", "Calle 123")

clinica.agregar_paciente(paciente1)

print(f"Paciente {paciente1.nombre} registrado con éxito en la clínica {clinica .nombre}.")

# el paciente se dirige al doctor para un chequeo

# el segundo paciente llega a la clínica y le consulta su dia programado para una consulta

print("Segundo paciente llega a la clínica y le consulta su dia programado para una consulta.")

# la recepcionista le pregunta su nombre y edad

nombre_paciente2 = input("Ingrese su nombre: ")

edad_paciente2 = input("Ingrese su edad: ")

dni_paciente2 = input("Ingrese su DNI: ")

# la recepcionista busca al paciente en el sistema 
#fecha programada el dia viernes a las 10:00 am
print("Recepcionista busca al paciente en el sistema.")

print("Fecha programada el dia viernes a las 10:00 am.")

#la recepcionista le informacion y guarda para no equivocarse

print(f"Recepcionista le informa al paciente {nombre_paciente2} sobre su cita programada para el dia viernes a las 10:00 am.")

#la recepcionista guarda la información para no equivocarse

print("Recepcionista guarda la información para no equivocarse.")

#el primer paciente regresa para pagar su consulta y pruebas de su posible diagnóstico y enfermedad

print("Primer paciente regresa para pagar su consulta y pruebas de su posible diagnóstico y enfermedad.")

#la recepcionista le pregunta su nombre para buscar su información

nombre_paciente1_pago = input("Ingrese su nombre para buscar su información: ")

#la recepcionista busca al paciente en el sistema y le muestra el monto a pagar

print(f"Recepcionista busca al paciente {nombre_paciente1_pago} en el sistema y le muestra el monto a pagar.")

#el paciente paga y se retira de la clínica

print(f"Paciente {nombre_paciente1_pago} paga y se retira de la clínica.")

#el segundo paciente regresa para pagar su consulta y pruebas de su posible diagnóstico y enfermedad

print("Segundo paciente regresa para pagar su consulta y pruebas de su posible diagnóstico y enfermedad.")

#la recepcionista le pregunta su nombre para buscar su información

nombre_paciente2_pago = input("Ingrese su nombre para buscar su información: ")

#la recepcionista busca al paciente en el sistema y le muestra el monto a pagar

print(f"Recepcionista busca al paciente {nombre_paciente2_pago} en el sistema y le muestra el monto a pagar.")

#el paciente paga y se retira de la clínica

print(f"Paciente {nombre_paciente2_pago} paga y se retira de la clínica.")

