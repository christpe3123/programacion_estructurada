# login.py

# Función de autenticar modificada para soportar ambos roles
def autenticar(usuario, contraseña):
    if usuario == "admin" and contraseña == "root":
        return "admin"
    elif usuario == "juan" and contraseña == "1234":
        return "usuario"
    else:
        return False

# Función de tokenizar / encriptar el token generado
def tokenmisar(usuario):
    if usuario == "admin" or usuario == "juan":
        return str(hash(usuario + "token"))
    else:
        return "00:00:00"

# Función alertar
def alertar(usuario):
    if usuario == "admin" or usuario == "juan":
        return "Alerta: Acceso concedido"
    else:
        return "Alerta: Acceso denegado"

# Función redirigir
def redirigir(usuario):
    if usuario == "admin":
        return "Bienvenido al panel de administración"
    elif usuario == "juan":
        return "Bienvenido usuario"
    else:
        return "Usuario no autorizado"