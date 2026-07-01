import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
from pathlib import Path
import login

BASE_DIR = Path(__file__).resolve().parent


def obtener_ruta_imagen(nombre):
    rutas = [BASE_DIR / nombre, BASE_DIR / "imagenes" / nombre]
    for ruta in rutas:
        if ruta.exists():
            return ruta
    return rutas[0]


# =========================
# VENTANA PRINCIPAL (LOGIN)
# =========================
ventana = tk.Tk()
ventana.geometry("500x670")
ventana.title("Sistema Login")
ventana.resizable(False, False)

menu_state = {"frame": None, "parent": None, "anim_id": None}


def cargar_imagen(nombre, tamaño):
    ruta = obtener_ruta_imagen(nombre)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró la imagen: {ruta}")

    imagen = Image.open(ruta)
    imagen = imagen.resize(tamaño)
    return ImageTk.PhotoImage(imagen)


def crear_boton(parent, text, command=None, bg="#ffffff", fg="#1a365d", bold=False, **kwargs):
    return tk.Button(
        parent,
        text=text,
        font=("Arial", 10, "bold" if bold else "normal"),
        bg=bg,
        fg=fg,
        relief="flat",
        command=command,
        **kwargs,
    )


# =========================
# FUNCIÓN: VENTANA DE REGISTRO
# =========================
def ventana_registro():
    ventana_reg = tk.Toplevel(ventana)
    ventana_reg.title("Crear Nueva Cuenta")
    ventana_reg.geometry("350x300")
    ventana_reg.grab_set()

    tk.Label(ventana_reg, text="Registro de Usuario", font=("Arial", 16, "bold")).pack(pady=15)

    tk.Label(ventana_reg, text="Nuevo Usuario:").pack(pady=2)
    entry_reg_usuario = tk.Entry(ventana_reg)
    entry_reg_usuario.pack(pady=5)

    tk.Label(ventana_reg, text="Nueva Contraseña:").pack(pady=2)
    entry_reg_pass = tk.Entry(ventana_reg, show="*")
    entry_reg_pass.pack(pady=5)

    def procesar_registro():
        user = entry_reg_usuario.get().strip()
        pas = entry_reg_pass.get().strip()
        resultado = login.registrar_usuario(user, pas)

        if resultado == "Éxito":
            messagebox.showinfo("Registro", f"¡Cuenta '{user}' creada con éxito!\nYa puedes iniciar sesión.")
            ventana_reg.destroy()
        else:
            messagebox.showerror("Error de Registro", resultado)

    crear_boton(
        ventana_reg,
        text="Guardar Cuenta",
        command=procesar_registro,
        bg="#2a9d8f",
        fg="white",
        bold=True,
    ).pack(pady=20)


# =========================
# FUNCIÓN: ANIMACIÓN DEL MENÚ DESPLEGABLE
# =========================
def animar_menu(frame, target_height, ventana_padre):
    if frame is None:
        return

    current_height = frame.winfo_height()
    step = 18 if target_height > current_height else -18
    next_height = current_height + step

    if (target_height > current_height and next_height >= target_height) or (
        target_height < current_height and next_height <= target_height
    ):
        next_height = target_height

    frame.place_configure(height=next_height)

    if next_height != target_height:
        menu_state["anim_id"] = ventana_padre.after(10, lambda: animar_menu(frame, target_height, ventana_padre))
    else:
        if target_height == 0:
            frame.destroy()
            menu_state["frame"] = None
            menu_state["parent"] = None
            menu_state["anim_id"] = None
        else:
            menu_state["anim_id"] = None


def toggle_menu(ventana_padre, usuario):
    if menu_state["frame"] is not None:
        if menu_state["anim_id"] is not None:
            ventana_padre.after_cancel(menu_state["anim_id"])
        animar_menu(menu_state["frame"], 0, ventana_padre)
        return

    frame = tk.Frame(ventana_padre, bg="#1a365d", bd=1, relief="solid")
    frame.place(x=230, y=55, width=250, height=0)

    tk.Label(frame, text="Configuración", font=("Arial", 11, "bold"), bg="#1a365d", fg="white").pack(pady=10)

    crear_boton(
        frame,
        text="📊 Detalles de Sesión",
        command=lambda: mostrar_detalles_sesion(usuario, ventana_padre),
    ).pack(pady=5, fill="x", padx=20)

    crear_boton(
        frame,
        text="🖼️ Ver Galería",
        command=lambda: mostrar_imagen(ventana_padre),
    ).pack(pady=5, fill="x", padx=20)

    tk.Label(frame, text="-----------------------", bg="#1a365d", fg="white").pack(pady=5)

    def cerrar_sesion():
        if menu_state["frame"] is not None:
            if menu_state["anim_id"] is not None:
                ventana_padre.after_cancel(menu_state["anim_id"])
            menu_state["frame"].destroy()
            menu_state["frame"] = None
            menu_state["parent"] = None
        ventana_padre.destroy()
        ventana.deiconify()

    crear_boton(
        frame,
        text="🚪 Cerrar Sesión",
        command=cerrar_sesion,
        bg="#e53e3e",
        fg="white",
        bold=True,
    ).pack(pady=5, fill="x", padx=20)

    menu_state["frame"] = frame
    menu_state["parent"] = ventana_padre
    animar_menu(frame, 240, ventana_padre)


# =========================
# VENTANA: PANEL DE PRESENTACIÓN (CON IMAGEN DE FONDO)
# =========================
def abrir_panel_usuario(usuario):
    ventana.withdraw()

    ventana_panel = tk.Toplevel(ventana)
    ventana_panel.title(f"Panel - {usuario.capitalize()}")
    ventana_panel.geometry("500x600")
    ventana_panel.resizable(False, False)
    ventana_panel.protocol("WM_DELETE_WINDOW", ventana.destroy)

    try:
        foto_fondo = cargar_imagen("cool-iphone-home-screen-80tba5zgx45jfo5r.jpg", (500, 600))
        label_fondo = tk.Label(ventana_panel, image=foto_fondo)
        label_fondo.image = foto_fondo
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error al cargar fondo: {e}")
        ventana_panel.configure(bg="#1A365D")

    btn_menu_esquina = crear_boton(
        ventana_panel,
        text="⚙️ Configuración",
        command=lambda: toggle_menu(ventana_panel, usuario),
        bg="#00b4d8",
        fg="white",
        bold=True,
    )
    btn_menu_esquina.place(x=350, y=15, width=130, height=35)

    try:
        foto_principal = cargar_imagen("cool-iphone-home-screen-80tba5zgx45jfo5r.jpg", (300, 180))
        label_principal = tk.Label(ventana_panel, image=foto_principal, bg="#142c4c")
        label_principal.image = foto_principal
        label_principal.place(x=100, y=220)
    except Exception as e:
        print(f"No se pudo cargar la imagen principal: {e}")

    tk.Label(
        ventana_panel,
        text="¡Sesión Iniciada!",
        font=("Arial", 22, "bold"),
        fg="#ffffff",
        bg="#142c4c",
    ).pack(pady=(120, 10))

    tk.Label(
        ventana_panel,
        text=f"Bienvenido de vuelta, {usuario.capitalize()}",
        font=("Arial", 14),
        fg="#a0aec0",
        bg="#142c4c",
    ).pack(pady=10)


# =========================
# VENTANA: DETALLES DE SESIÓN
# =========================
def mostrar_detalles_sesion(usuario, ventana_padre):
    ventana_detalles = tk.Toplevel(ventana_padre)
    ventana_detalles.title("Detalles de la Sesión")
    ventana_detalles.geometry("400x250")

    ahora = datetime.now()
    dia_actual = ahora.strftime("%d/%m/%Y")
    hora_actual = ahora.strftime("%H:%M:%S")
    token_generado = login.tokenmisar(usuario)

    frame_info = tk.LabelFrame(
        ventana_detalles,
        text=" Datos de Ingreso ",
        font=("Arial", 10, "italic"),
        padx=15,
        pady=15,
    )
    frame_info.pack(pady=20, fill="both", expand=True, padx=20)

    tk.Label(frame_info, text=f"📆 Día de ingreso: {dia_actual}", font=("Arial", 11)).pack(anchor="w", pady=5)
    tk.Label(frame_info, text=f"⏰ Hora de ingreso: {hora_actual}", font=("Arial", 11)).pack(anchor="w", pady=5)
    tk.Label(frame_info, text=f"🔑 Token: {token_generado}", font=("Arial", 11, "bold"), fg="darkblue").pack(anchor="w", pady=5)


# =========================
# VENTANA: MOSTRAR IMAGEN INTERNA
# =========================
def mostrar_imagen(ventana_padre):
    ventana_img = tk.Toplevel(ventana_padre)
    ventana_img.title("Imagen de Bienvenida")
    ventana_img.geometry("400x420")

    try:
        foto = cargar_imagen("cool-iphone-home-screen-80tba5zgx45jfo5r.jpg", (250, 250))
        label_imagen = tk.Label(ventana_img, image=foto)
        label_imagen.image = foto
        label_imagen.pack(pady=15)
    except Exception as e:
        tk.Label(ventana_img, text=f"No se pudo cargar la imagen\n{e}", fg="red").pack(pady=20)

    tk.Label(ventana_img, text="A pero para pedir Plata, son buenos", font=("Arial", 14, "bold")).pack(pady=10)


# =========================
# ACCIONES DE LOGEO
# =========================
def login_usuario():
    usuario = entry_usuario.get().strip()
    password = entry_password.get().strip()
    resultado = login.autenticar(usuario, password)

    if resultado:
        print(login.alertar(usuario))
        messagebox.showinfo("Usuario", login.redirigir(usuario))
        abrir_panel_usuario(usuario)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


def login_admin():
    admin = entry_admin.get().strip()
    admin_password = entry_admin_password.get().strip()
    resultado = login.autenticar(admin, admin_password)

    if resultado == "admin":
        print(login.alertar(admin))
        messagebox.showinfo("Administrador", login.redirigir(admin))
        abrir_panel_usuario(admin)
    else:
        messagebox.showerror("Error", "Acceso administrador incorrecto")


# =========================
# INTERFAZ GRÁFICA DE LOGIN
# =========================
frame_login = tk.Frame(ventana)
frame_login.pack(pady=10)

try:
    logo = cargar_imagen("images.jpg", (120, 120))
    logo_label = tk.Label(frame_login, image=logo)
    logo_label.image = logo
    logo_label.pack(pady=5)
except Exception:
    tk.Label(frame_login, text="[LOGO]", font=("Arial", 14)).pack(pady=5)

tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 20, "bold")).pack(pady=10)

# Campos de inicio normal
tk.Label(frame_login, text="Usuario").pack()
entry_usuario = tk.Entry(frame_login)
entry_usuario.pack(pady=5)
tk.Label(frame_login, text="Contraseña").pack()
entry_password = tk.Entry(frame_login, show="*")
entry_password.pack(pady=5)
tk.Button(frame_login, text="Entrar Usuario", bg="blue", fg="white", command=login_usuario).pack(pady=5)

tk.Label(frame_login, text="----------------------").pack(pady=5)

# Campos de administrador
tk.Label(frame_login, text="Administrador").pack()
entry_admin = tk.Entry(frame_login)
entry_admin.pack(pady=5)
tk.Label(frame_login, text="Contraseña Admin").pack()
entry_admin_password = tk.Entry(frame_login, show="*")
entry_admin_password.pack(pady=5)
tk.Button(frame_login, text="Entrar Admin", bg="red", fg="white", command=login_admin).pack(pady=5)

tk.Label(frame_login, text="----------------------").pack(pady=5)

btn_crear_cuenta = tk.Button(
    frame_login,
    text="¿No tienes cuenta? Regístrate aquí",
    font=("Arial", 10, "underline"),
    fg="#0077b6",
    bd=0,
    cursor="hand2",
    command=ventana_registro,
)
btn_crear_cuenta.pack(pady=10)

ventana.mainloop()