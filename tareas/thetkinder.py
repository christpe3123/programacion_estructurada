import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.geometry("500x400")
ventana.title("Login")

# Título
titulo = tk.Label(
    ventana,
    text="Iniciar Sesión",
    font=("Arial", 24)
)
titulo.pack(pady=40)

# Usuario
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack()

entry_usuario = tk.Entry(ventana, width=30)
entry_usuario.pack(pady=10)

# Contraseña
label_password = tk.Label(ventana, text="Contraseña:")
label_password.pack()

entry_password = tk.Entry(ventana, width=30, show="*")
entry_password.pack(pady=10)

#administrador
label_admin = tk.Label(ventana, text="Administrador:")
label_admin.pack()
entry_admin = tk.Entry(ventana, width=30)
entry_admin.pack(pady=10)


# Función login
def login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    print("Usuario:", usuario)
    print("Contraseña:", password)

# Botón
boton_login = tk.Button(
    ventana,
    text="Ingresar",
    command=login
)
boton_login.pack(pady=30)

# Ejecutar
ventana.mainloop()