import login    
def mostrar_plataforma(usuario):
    if login.autenticar(usuario.usuario, usuario.contraseña):
        token = login.tokenmisar(usuario.usuario)
        alerta = login.alertar(usuario.usuario)
        redireccion = login.redirigir(usuario.usuario)
        return f"Bienvenido a la plataforma, {usuario.usuario}!\n{alerta}\nToken: {token}\n{redireccion}"
    else:
        return "Error: No se pudo acceder a la plataforma debido a credenciales incorrectas"