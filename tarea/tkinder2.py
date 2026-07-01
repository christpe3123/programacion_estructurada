import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime  
import login  

# =========================
# VENTANA PRINCIPAL (LOGIN)
# =========================
ventana = tk.Tk()
ventana.geometry("500x600")
ventana.title("Sistema Login")

# Variable global para rastrear si el menú de la esquina está abierto o cerrado
menu_desplegado = False
frame_menu_desplegable = None

# =========================
# FUNCIÓN: INTERRUPTOR DEL MENÚ DESPLEGABLE (TOGGLE)
# =========================
def toggle_menu(ventana_padre, usuario):
    global menu_desplegado, frame_menu_desplegable
    
    if menu_desplegado:
        frame_menu_desplegable.destroy()
        menu_desplegado = False
    else:
        menu_desplegado = True
        
        # Frame contenedor con fondo ligeramente oscuro para que resalte sobre el fondo azul
        frame_menu_desplegable = tk.Frame(ventana_padre, bg="#1a365d", bd=1, relief="solid")
        frame_menu_desplegable.place(x=230, y=55, width=250, height=240)
        
        tk.Label(
            frame_menu_desplegable, 
            text="Menú de Opciones", 
            font=("Arial", 11, "bold"), 
            bg="#1a365d",
            fg="white"
        ).pack(pady=10)
        
        # Opción 1: Ver detalles de la sesión
        tk.Button(
            frame_menu_desplegable,
            text="📊 Detalles de Sesión",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#1a365d",
            activebackground="#e2e8f0",
            command=lambda: mostrar_detalles_sesion(usuario, ventana_padre)
        ).pack(pady=5, fill="x", padx=20)

        # Opción 2: Ver Imagen de bienvenida
        tk.Button(
            frame_menu_desplegable,
            text="🖼️ Ver Galería",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#1a365d",
            activebackground="#e2e8f0",
            command=lambda: mostrar_imagen(ventana_padre)
        ).pack(pady=5, fill="x", padx=20)

        # Separador
        tk.Label(frame_menu_desplegable, text="-----------------------", bg="#1a365d", fg="white").pack(pady=5)

        # Opción 3: Cerrar Sesión
        def cerrar_sesion():
            global menu_desplegado
            menu_desplegado = False
            ventana_padre.destroy()
            ventana.deiconify() 

        tk.Button(
            frame_menu_desplegable,
            text="🚪 Cerrar Sesión",
            font=("Arial", 10, "bold"),
            bg="#e53e3e",
            fg="white",
            activebackground="#c53030",
            command=cerrar_sesion
        ).pack(pady=5, fill="x", padx=20)


# =========================
# VENTANA: PANEL TRAS LOGUEARSE (PANTALLA DE PRESENTACIÓN)
# =========================
def abrir_panel_usuario(usuario):
    global menu_desplegado
    menu_desplegado = False 
    
    ventana.withdraw()

    ventana_panel = tk.Toplevel(ventana)
    ventana_panel.title(f"Panel - {usuario.capitalize()}")
    ventana_panel.geometry("500x600")
    ventana_panel.resizable(False, False) # Mantenemos fijo el tamaño para el fondo
    
    ventana_panel.protocol("WM_DELETE_WINDOW", ventana.destroy)

    # --- IMPLEMENTACIÓN DE LA IMAGEN DE FONDO ---
    try:
        # Cargar y redimensionar la imagen dcc6b79cd9c69f128b769a8e97b562e7.jpg
        img_fondo = Image.open("dcc6b79cd9c69f128b769a8e97b562e7.jpg")
        img_fondo = img_fondo.resize((500, 600))
        foto_fondo = ImageTk.PhotoImage(img_fondo)
        
        # Colocar el fondo cubriendo toda la ventana
        label_fondo = tk.Label(ventana_panel, image=foto_fondo)
        label_fondo.image = foto_fondo # Mantener referencia
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error al cargar el fondo dcc6b79cd9c69f128b769a8e97b562e7.jpg: {e}")
        ventana_panel.configure(bg="#1A365D") # Fondo azul alternativo si falla

    # --- BOTÓN EN LA ESQUINA SUPERIOR DERECHA ---
    btn_menu_esquina = tk.Button(
        ventana_panel,
        text="☰ Menú",
        font=("Arial", 11, "bold"),
        bg="#00b4d8",
        fg="white",
        relief="flat",
        activebackground="#0077b6",
        activeforeground="white",
        command=lambda: toggle_menu(ventana_panel, usuario)
    )
    btn_menu_esquina.place(x=390, y=15, width=90, height=35)

    # --- TEXTOS EN LA PANTALLA ---
    # Usamos bg="#173054" (aproximado al azul de la imagen) o dejamos que contraste
    tk.Label(
        ventana_panel, 
        text="¡Sesión Iniciada!", 
        font=("Arial", 22, "bold"),
        fg="#ffffff",
        bg="#142c4c" # Color de fondo adaptado a la zona central de la imagen
    ).pack(pady=(120, 10))
    
    tk.Label(
        ventana_panel, 
        text=f"Bienvenido de vuelta, {usuario.capitalize()}", 
        font=("Arial", 14),
        fg="#a0aec0",
        bg="#142c4c"
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
        pady=15
    )
    frame_info.pack(pady=20, fill="both", expand=True, padx=20)

    tk.Label(frame_info, text=f"📆 Día de ingreso: {dia_actual}", font=("Arial", 11)).pack(anchor="w", pady=5)
    tk.Label(frame_info, text=f"⏰ Hora de ingreso: {hora_actual}", font=("Arial", 11)).pack(anchor="w", pady=5)
    tk.Label(frame_info, text=f"🔑 Token: {token_generado}", font=("Arial", 11, "bold"), fg="darkblue").pack(anchor="w", pady=5)


# =========================
# VENTANA: MOSTRAR IMAGEN (Galería interna)
# =========================
def mostrar_imagen(ventana_padre):  
    ventana_img = tk.Toplevel(ventana_padre)
    ventana_img.title("Imagen de Bienvenida")
    ventana_img.geometry("400x420")  

    try:
        imagen = Image.open("tarea/imagenes/bienvenido.jpg")
        imagen = imagen.resize((250, 250))
        foto = ImageTk.PhotoImage(imagen)

        label_imagen = tk.Label(ventana_img, image=foto)
        label_imagen.image = foto  
        label_imagen.pack(pady=15)
    except Exception as e:
        tk.Label(ventana_img, text=f"No se pudo cargar la imagen\n{e}", fg="red").pack(pady=20)

    tk.Label(
        ventana_img,
        text="A pero para pedir Plata, son buenos",
        font=("Arial", 14, "bold")
    ).pack(pady=10)


# =========================
# LOGINES Y CONFIGURACIÓN DE INICIO
# =========================
def login_usuario():
    usuario = entry_usuario.get()
    password = entry_password.get()
    resultado = login.autenticar(usuario, password)

    if resultado == "usuario":
        print(login.alertar(usuario))  
        messagebox.showinfo("Usuario", login.redirigir(usuario))
        abrir_panel_usuario(usuario)  
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def login_admin():
    admin = entry_admin.get()
    admin_password = entry_admin_password.get()
    resultado = login.autenticar(admin, admin_password)

    if resultado == "admin":
        print(login.alertar(admin))  
        messagebox.showinfo("Administrador", login.redirigir(admin))
        abrir_panel_usuario(admin)  
    else:
        messagebox.showerror("Error", "Acceso administrador incorrecto")

frame_login = tk.Frame(ventana)
frame_login.pack(pady=20)

try:
    logo_image = Image.open("tarea/imagenes/images.jpg")
    logo_image = logo_image.resize((150, 150))
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(frame_login, image=logo)
    logo_label.pack(pady=10)
except Exception:
    tk.Label(frame_login, text="[LOGO]", font=("Arial", 14)).pack(pady=10)

tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 24)).pack(pady=20)

# Campos Usuario
tk.Label(frame_login, text="Usuario").pack()
entry_usuario = tk.Entry(frame_login)
entry_usuario.pack(pady=5)
tk.Label(frame_login, text="Contraseña").pack()
entry_password = tk.Entry(frame_login, show="*")
entry_password.pack(pady=10)
tk.Button(frame_login, text="Entrar Usuario", bg="blue", fg="white", command=login_usuario).pack(pady=10)

tk.Label(frame_login, text="----------------------").pack(pady=10)

# Campos Admin
tk.Label(frame_login, text="Administrador").pack()
entry_admin = tk.Entry(frame_login)
entry_admin.pack(pady=5)
tk.Label(frame_login, text="Contraseña Admin").pack()
entry_admin_password = tk.Entry(frame_login, show="*")
entry_admin_password.pack(pady=10)
tk.Button(frame_login, text="Entrar Admin", bg="red", fg="white", command=login_admin).pack(pady=10)

ventana.mainloop()