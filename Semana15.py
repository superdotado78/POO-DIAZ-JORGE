import tkinter as tk
from tkinter import messagebox

# Función para añadir tareas
def add_task(event=None):
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Debes escribir una tarea.")

# Función para marcar tareas como completadas
def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task_text = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, f"{task_text} - Completada")
    except IndexError:
        messagebox.showwarning("Selección", "Debes seleccionar una tarea primero.")

# Función para eliminar tareas
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selección", "Debes seleccionar una tarea primero.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Añadir tarea con la tecla Enter

# Botón para añadir tareas
add_button = tk.Button(root, text="Añadir Tarea", width=40, command=add_task)
add_button.pack(pady=5)

# Listbox para mostrar las tareas
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Botón para marcar como completada
complete_button = tk.Button(root, text="Marcar como Completada", width=40, command=complete_task)
complete_button.pack(pady=5)

# Botón para eliminar tareas
delete_button = tk.Button(root, text="Eliminar Tarea", width=40, command=delete_task)
delete_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
