# login.py

usuarios_registrados = {
    "admin": {"contraseña": "root", "rol": "admin"},
    "juan": {"contraseña": "1234", "rol": "usuario"},
}


def autenticar(usuario, contraseña):
    datos = usuarios_registrados.get(usuario)
    if datos and datos["contraseña"] == contraseña:
        return datos["rol"]
    return False


def registrar_usuario(usuario, contraseña):
    usuario = usuario.strip()
    contraseña = contraseña.strip()

    if not usuario or not contraseña:
        return "Error: Campos vacíos"
    if usuario in usuarios_registrados:
        return "Error: El usuario ya existe"

    usuarios_registrados[usuario] = {"contraseña": contraseña, "rol": "usuario"}
    return "Éxito"


def tokenmisar(usuario):
    if usuario in usuarios_registrados:
        return str(hash(usuario + "token"))
    return "00:00:00"


def alertar(usuario):
    if usuario in usuarios_registrados:
        return "Alerta: Acceso concedido"
    return "Alerta: Acceso denegado"


def redirigir(usuario):
    datos = usuarios_registrados.get(usuario)
    if not datos:
        return "Usuario no autorizado"
    if datos["rol"] == "admin":
        return "Bienvenido al panel de administración"
    return f"Bienvenido usuario: {usuario}"