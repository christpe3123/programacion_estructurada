import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime  # <-- Importamos para capturar día y hora
import login  # <-- Importamos tu archivo de lógica de login

# =========================
# VENTANA PRINCIPAL
# =========================
ventana = tk.Tk()
ventana.geometry("500x600")
ventana.title("Sistema Login")

# =========================
# MOSTRAR NUEVA VENTANA
# =========================
def mostrar_imagen(usuario):  
    # Ocultamos la ventana de inicio de sesión
    ventana.withdraw()

    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Bienvenido")
    nueva_ventana.geometry("500x650")  

    # Al cerrar la ventana de bienvenida con la "X", cerramos todo el programa por completo
    nueva_ventana.protocol("WM_DELETE_WINDOW", ventana.destroy)

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

    # Mensaje de éxito
    tk.Label(
        nueva_ventana,
        text="A pero para pedir Plata, son buenos",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # --- OBTENER DATOS DE TIEMPO Y TOKEN ---
    ahora = datetime.now()
    dia_actual = ahora.strftime("%d/%m/%Y")
    hora_actual = ahora.strftime("%H:%M:%S")
    token_generado = login.tokenmisar(usuario)  

    # --- CUADRO DE DETALLES DE SESIÓN ---
    frame_info = tk.LabelFrame(
        nueva_ventana, 
        text=" Detalles de la Sesión ", 
        font=("Arial", 10, "italic"), 
        padx=15, 
        pady=10
    )
    frame_info.pack(pady=10, fill="x", padx=40)

    # Mostramos los datos solicitados
    tk.Label(frame_info, text=f"📆 Día de ingreso: {dia_actual}", font=("Arial", 11)).pack(anchor="w", pady=2)
    tk.Label(frame_info, text=f"⏰ Hora de ingreso: {hora_actual}", font=("Arial", 11)).pack(anchor="w", pady=2)
    tk.Label(frame_info, text=f"🔑 Token: {token_generado}", font=("Arial", 11, "bold"), fg="darkblue").pack(anchor="w", pady=2)


# =========================
# LOGIN USUARIO
# =========================
def login_usuario():
    usuario = entry_usuario.get()
    password = entry_password.get()

    # Validamos usando la función del archivo login.py
    resultado = login.autenticar(usuario, password)

    if resultado == "usuario":
        print(login.alertar(usuario))  
        messagebox.showinfo("Usuario", login.redirigir(usuario))
        mostrar_imagen(usuario)  
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# =========================
# LOGIN ADMINISTRADOR
# =========================
def login_admin():
    admin = entry_admin.get()
    admin_password = entry_admin_password.get()

    # Validamos usando la función del archivo login.py
    resultado = login.autenticar(admin, admin_password)

    if resultado == "admin":
        print(login.alertar(admin))  
        messagebox.showinfo("Administrador", login.redirigir(admin))
        mostrar_imagen(admin)  
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
try:
    logo_image = Image.open("tarea/imagenes/images.jpg")
    logo_image = logo_image.resize((150, 150))
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(frame_login, image=logo)
    logo_label.pack(pady=10)
except Exception:
    tk.Label(frame_login, text="[LOGO]", font=("Arial", 14)).pack(pady=10)

# =========================
# TITULO
# =========================
tk.Label(
    frame_login,
    text="Iniciar Sesión",
    font=("Arial", 24)
).pack(pady=20)

# =========================
# USUARIO NORMAL
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