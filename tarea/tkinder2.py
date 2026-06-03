import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import login

# =========================
# DATOS
# =========================
# Usuario normal
USUARIO =   "juan"
PASSWORD = "1234"
# Administrador
ADMIN = "admin"
ADMIN_PASSWORD = "root"

# =========================
# VENTANA PRINCIPAL
# =========================
ventana = tk.Tk()
ventana.geometry("500x600")
ventana.title("Sistema Login")

# =========================
# MOSTRAR NUEVA VENTANA
# =========================
def mostrar_imagen():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Bienvenido")
    nueva_ventana.geometry("500x500")

    try:
        # Cargar imagen
        imagen = Image.open("tarea/imagenes/bienvenido.jpg")
        imagen = imagen.resize((300, 300))

        foto = ImageTk.PhotoImage(imagen)

        # Mostrar imagen
        label_imagen = tk.Label(nueva_ventana, image=foto)
        label_imagen.image = foto  # Mantener referencia
        label_imagen.pack(pady=20)

    except Exception as e:
        tk.Label(
            nueva_ventana,
            text=f"No se pudo cargar la imagen\n{e}",
            fg="red"
        ).pack(pady=20)

    tk.Label(
        nueva_ventana,
        text="Iniciaste sesion fracasado",
        font=("Arial", 16)
    ).pack()

# =========================
# LOGIN USUARIO
# =========================
def login_usuario():
    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == USUARIO and password == PASSWORD:
        messagebox.showinfo("Usuario", "Bienvenido usuario")
        mostrar_imagen()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# =========================
# LOGIN ADMIN
# =========================
def login_admin():
    admin = entry_admin.get()
    admin_password = entry_admin_password.get()

    if admin == ADMIN and admin_password == ADMIN_PASSWORD:
        messagebox.showinfo("Administrador", "Bienvenido administrador")
        mostrar_imagen()
    else:
        messagebox.showerror("Error", "Acceso administrador incorrecto")

# =========================
# FRAME LOGIN
# =========================
frame_login = tk.Frame(ventana)
frame_login.pack(pady=20)

# =========================
# LOGO
# =========================
logo_image = Image.open("tarea/imagenes/images.jpg")
logo_image = logo_image.resize((150, 150))

logo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(frame_login, image=logo)
logo_label.pack(pady=10)

# =========================
# TITULO
# =========================
tk.Label(
    frame_login,
    text="Iniciar Sesión",
    font=("Arial", 24)
).pack(pady=20)

# =========================
# USUARIO
# =========================
tk.Label(frame_login, text="Usuario").pack()

entry_usuario = tk.Entry(frame_login)
entry_usuario.pack(pady=5)

tk.Label(frame_login, text="Contraseña").pack()

entry_password = tk.Entry(frame_login, show="*")
entry_password.pack(pady=10)

tk.Button(
    frame_login,
    text="Entrar Usuario",
    bg="blue",
    fg="white",
    command=login_usuario
).pack(pady=10)

# =========================
# SEPARADOR
# =========================
tk.Label(
    frame_login,
    text="----------------------"
).pack(pady=10)

# =========================
# ADMINISTRADOR
# =========================
tk.Label(frame_login, text="Administrador").pack()

entry_admin = tk.Entry(frame_login)
entry_admin.pack(pady=5)

tk.Label(frame_login, text="Contraseña Admin").pack()

entry_admin_password = tk.Entry(frame_login, show="*")
entry_admin_password.pack(pady=10)

tk.Button(
    frame_login,
    text="Entrar Admin",
    bg="red",
    fg="white",
    command=login_admin
).pack(pady=10)

# =========================
# EJECUTAR
# =========================
ventana.mainloop()