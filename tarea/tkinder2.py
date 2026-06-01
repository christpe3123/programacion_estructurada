import tkinter as tk
from tkinter import messagebox

# =========================
# DATOS
# =========================
USUARIO = "juan"
PASSWORD = "1234"

ADMIN = "admin"
ADMIN_PASSWORD = "root"

# =========================
# VENTANA
# =========================
ventana = tk.Tk()
ventana.geometry("500x600")
ventana.title("Sistema Login")

# =========================
# MOSTRAR IMAGEN
# =========================
def mostrar_imagen():

    frame_login.pack_forget()
    frame_imagen.pack(pady=20)

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

tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 24)).pack(pady=20)

# Usuario
tk.Label(frame_login, text="Usuario").pack()
entry_usuario = tk.Entry(frame_login)
entry_usuario.pack(pady=5)

tk.Label(frame_login, text="Contraseña").pack()
entry_password = tk.Entry(frame_login, show="*")
entry_password.pack(pady=10)

tk.Button(frame_login, text="Entrar Usuario", bg="blue", fg="white",
          command=login_usuario).pack(pady=10)

tk.Label(frame_login, text="----------------------").pack(pady=10)

# Admin
tk.Label(frame_login, text="Administrador").pack()
entry_admin = tk.Entry(frame_login)
entry_admin.pack(pady=5)

tk.Label(frame_login, text="Contraseña Admin").pack()
entry_admin_password = tk.Entry(frame_login, show="*")
entry_admin_password.pack(pady=10)

tk.Button(frame_login, text="Entrar Admin", bg="red", fg="white",
          command=login_admin).pack(pady=10)

# =========================
# FRAME IMAGEN
# =========================
frame_imagen = tk.Frame(ventana)

tk.Label(frame_imagen, text="Bienvenido", font=("Arial", 20)).pack(pady=20)

# Cargar imagen PNG o GIF
imagen = tk.PhotoImage(file=r"C:\Users\PC-01\Documents\GitHub\programacion_estructurada\tarea\imagen.png")

label_img = tk.Label(frame_imagen, image=imagen)
label_img.image = imagen  # importante
label_img.pack()

# =========================
# EJECUTAR
# =========================
ventana.mainloop()