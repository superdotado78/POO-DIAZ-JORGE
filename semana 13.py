import tkinter as tk
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar_dato():
    texto = entrada.get()
    if texto:
        lista_datos.insert(tk.END, texto)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos (Jorge Dìaz)")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresar texto:")
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botón para agregar dato
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el loop de la ventana
ventana.mainloop()
