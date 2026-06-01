import tkinter as tk
from tkinter import messagebox

# =========================
# DATOS
# =========================

# Usuario normal
USUARIO = "juan"
PASSWORD = "1234"

# Administrador
ADMIN = "admin"
ADMIN_PASSWORD = "root"

# =========================
# VENTANA
# =========================
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Sistema Login")

# =========================
# TITULO
# =========================
titulo = tk.Label(
    ventana,
    text="Iniciar Sesión",
    font=("Arial", 24)
)
titulo.pack(pady=20)

# ==================================================
# LOGIN USUARIO
# ==================================================

label_usuario = tk.Label(
    ventana,
    text="Usuario"
)
label_usuario.pack()

entry_usuario = tk.Entry(
    ventana,
    width=30
)
entry_usuario.pack(pady=5)

label_password = tk.Label(
    ventana,
    text="Contraseña"
)
label_password.pack()

entry_password = tk.Entry(
    ventana,
    width=30,
    show="*"
)
entry_password.pack(pady=10)

# =========================
# LOGIN USUARIO
# =========================
def login_usuario():

    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == USUARIO and password == PASSWORD:

        messagebox.showinfo(
            "Usuario",
            "Bienvenido usuario"
        )

    else:

        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )

boton_usuario = tk.Button(
    ventana,
    text="Entrar Usuario",
    command=login_usuario,
    bg="blue",
    fg="white"
)

boton_usuario.pack(pady=20)

# ==================================================
# SEPARADOR
# ==================================================

separador = tk.Label(
    ventana,
    text="----------------------"
)
separador.pack(pady=10)

# ==================================================
# LOGIN ADMINISTRADOR
# ==================================================

label_admin = tk.Label(
    ventana,
    text="Administrador"
)
label_admin.pack()

entry_admin = tk.Entry(
    ventana,
    width=30
)
entry_admin.pack(pady=5)

label_admin_password = tk.Label(
    ventana,
    text="Contraseña Admin"
)
label_admin_password.pack()

entry_admin_password = tk.Entry(
    ventana,
    width=30,
    show="*"
)
entry_admin_password.pack(pady=10)

# =========================
# LOGIN ADMIN
# =========================
def login_admin():

    admin = entry_admin.get()
    admin_password = entry_admin_password.get()

    if admin == ADMIN and admin_password == ADMIN_PASSWORD:

        messagebox.showinfo(
            "Administrador",
            "Bienvenido administrador"
        )

    else:

        messagebox.showerror(
            "Error",
            "Acceso administrador incorrecto"
        )

boton_admin = tk.Button(
    ventana,
    text="Entrar Admin",
    command=login_admin,
    bg="red",
    fg="white"
)

boton_admin.pack(pady=20)

# =========================
# EJECUTAR
# =========================
ventana.mainloop()