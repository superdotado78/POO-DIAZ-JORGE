import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Lista para almacenar las tareas
tareas = []

# Función para actualizar la lista de tareas en la interfaz gráfica
def actualizar_lista():
    lista_tareas.delete(0, tk.END)  # Limpiar la lista de la interfaz
    for tarea in tareas:
        estado = "✅" if tarea[1] else "❌"
        lista_tareas.insert(tk.END, f"{estado} {tarea[0]}")

# Función para añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea:
        tareas.append((tarea, False))  # (tarea, False) -> False significa no completada
        entrada_tarea.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar una tarea como completada
def marcar_completada(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        tareas[indice] = (tareas[indice][0], True)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea seleccionada
def eliminar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        del tareas[indice]
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

# Cerrar la aplicación con la tecla Escape
def cerrar_aplicacion(event=None):
    root.quit()

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

# Botones de la aplicación
boton_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.grid(row=0, column=1, padx=10, pady=10)

boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
boton_completar.grid(row=1, column=1, padx=10, pady=10)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

# Lista donde se mostrarán las tareas
lista_tareas = tk.Listbox(root, height=10, width=50)
lista_tareas.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

# Enlazar eventos de teclado
root.bind("<Return>", agregar_tarea)  # Tecla Enter para añadir tarea
root.bind("<c>", marcar_completada)   # Tecla "C" para completar tarea
root.bind("<d>", eliminar_tarea)      # Tecla "D" para eliminar tarea
root.bind("<Delete>", eliminar_tarea) # Tecla Delete para eliminar tarea
root.bind("<Escape>", cerrar_aplicacion)  # Tecla Escape para cerrar

# Iniciar bucle principal
root.mainloop()
