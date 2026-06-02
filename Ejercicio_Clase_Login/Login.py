import tkinter as tk
from tkinter import messagebox
import json
import os

BASE_DIR = os.path.dirname(__file__)
ARCHIVO_USUARIOS = os.path.join(BASE_DIR, "credenciales.json")

def limpiar_entradas():#Funcion para limpiar las credenciales ingresadas
    entrada_usuario.delete(0, tk.END)
    entrada_clave.delete(0, tk.END)

def ventana_principal():
    ventana_principal = tk.Toplevel(ventana)
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("1200x700")
    ventana_principal.configure(background="lightblue")

    mensaje_bienvenida = tk.Label(ventana_principal, text="¡Bienvenido a la Ventana Principal!", bg="lightblue", font=("Arial", 14))
    mensaje_bienvenida.pack(pady=50)

def validar_login():
    usuario = entrada_usuario.get()
    clave = entrada_clave.get()

    with open(ARCHIVO_USUARIOS, "r") as cred:
        credenciales = json.load(cred)

    if not usuario or not clave:
        messagebox.showwarning("Campos vacíos", "Por favor, ingresa tu usuario y clave.")
        return

    for user in credenciales["usuarios"]:
        if usuario == user["usuario"] and clave == user["clave"]:
            messagebox.showinfo("Login válido", f"Bienvenid@ {usuario}!")
            ventana_principal()
            ventana.withdraw()
            return

    messagebox.showerror("Login inválido", "Usuario o clave incorrectos. Inténtalo de nuevo.")
    limpiar_entradas()

ventana = tk.Tk()
ventana.title("Login_App")
ventana.geometry("1200x700")
ventana.configure(background="lightblue")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(12, weight=1)

titulo = tk.Label(ventana, text="Inicio de Sesión", bg="lightblue", font=("Arial", 16))
titulo.grid(row=0, column=6) 

entrada_usuario = tk.Entry(ventana,width=50, font=("Arial", 15), )
entrada_usuario.grid(row=1, column=6)

entrada_clave = tk.Entry(ventana, show="*", width=50, font=("Arial", 15))
entrada_clave.grid(row=2, column=6)

boton_ingresar = tk.Button(ventana, text="Ingresar", command=validar_login)
boton_ingresar.grid(row=3, column=6)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_entradas)#Limpiar las entradas
boton_limpiar.grid(row=4, column=6)

ventana.mainloop()