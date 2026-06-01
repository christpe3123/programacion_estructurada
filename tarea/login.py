#funcion de autenticar
def autenticar(usuario, contraseña):
    if usuario == "admin" and contraseña == "1234":
        return True
    else:
        return False

#funcion de tokenmisar
#increptimizar el token generado
def tokenmisar(usuario):
    if usuario == "admin":
        return "10:21:01"
    else:
        return "00:00:00"
    
#funcion alertar 
def alertar(usuario):
    if usuario == "admin":
        return "Alerta: Acceso concedido"
    else:
        return "Alerta: Acceso denegado"
#funcion redirigir
def redirigir(usuario):
    if usuario == "admin":
        return "Bienvenido al panel de administración"
    else:
        return "Usuario no autorizado"
