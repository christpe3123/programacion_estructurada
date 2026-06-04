import login    
class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def iniciar_sesion(self):
        if login.autenticar(self.usuario, self.contraseña):
            token = login.tokenmisar(self.usuario)
            alerta = login.alertar(self.usuario)
            redireccion = login.redirigir(self.usuario)
            return f"{alerta}\nToken: {token}\n{redireccion}"
        else:
            return "Error: Credenciales incorrectas"
# Ejemplo de uso
usuario1 = Usuario("admin", "1234")
print(usuario1.iniciar_sesion())
usuario2 = Usuario("user", "abcd")
print(usuario2.iniciar_sesion())